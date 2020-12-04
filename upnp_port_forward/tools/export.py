import logging
from typing import NamedTuple, Tuple

import upnpclient

from upnp_port_forward.exceptions import NoPortMapServiceFound


class UPnPServiceNames(NamedTuple):
    device_friendly_name: str
    device_location: str
    service_names: Tuple[str, ...]


def fetch_add_portmapping_services() -> Tuple[UPnPServiceNames, ...]:
    """
    :return: returns the available devices and services for which the action 'AddPortMapping' exists
    """
    devices = upnpclient.discover()
    if not devices:
        raise NoPortMapServiceFound("No UPnP devices available")

    services_with_AddPortMapping = []
    for upnp_dev in devices:
        service_names = []
        for service in upnp_dev.services:
            try:
                service["AddPortMapping"]
            except KeyError:
                continue
            else:
                service_names.append(service.name)

        if len(service_names) > 0:
            services_with_AddPortMapping.append(
                UPnPServiceNames(
                    upnp_dev.friendly_name, upnp_dev.location, tuple(service_names)
                )
            )

    if len(services_with_AddPortMapping) <= 0:
        raise NoPortMapServiceFound(
            "Unable to find a device with a port mapping service"
        )

    return tuple(services_with_AddPortMapping)


def main() -> None:
    logger = logging.getLogger("upnp_port_forward.tools.export")
    try:
        upnp_service_names_by_device = fetch_add_portmapping_services()
        service_names_output = "\n"
        for service in upnp_service_names_by_device:
            service_names_output = service_names_output.join(
                [
                    f"\n{'-' * 40}",
                    f"Device Name: {service.device_friendly_name}",
                    f"Device Location: {service.device_location}",
                    "Available UPnP services found on this device:",
                    "\n".join(
                        f"    {service_name}" for service_name in service.service_names
                    ),
                ]
            )
        service_names_output = "\n".join(
            [
                service_names_output,
                "You can now try to launch upnp_port_forward.client.setup_port_map()",
                "with required_service_names=(<service name>, ...)",
                "To help this library supports more routers, you can submit new service names",
                "here: https://github.com/ethereum/upnp-port-forward/issues - Thanks !!",
            ]
        )

        logging.basicConfig(level=logging.INFO)
        logger.info(service_names_output)

    except NoPortMapServiceFound:
        logger.error("No port mapping services found")


if __name__ == "__main__":
    main()
