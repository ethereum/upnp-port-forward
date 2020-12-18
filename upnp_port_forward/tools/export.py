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


def output_upnp_service_names(
    upnp_service_names_by_device: Tuple[UPnPServiceNames, ...]
) -> None:
    service_names_output = [
        f"\n{'-' * 40}",
    ]
    for service in upnp_service_names_by_device:
        service_names_output.extend(
            [
                f"Device Name:     {service.device_friendly_name}",
                f"Device Location: {service.device_location}",
                "Available UPnP services found on this device:",
            ]
        )
        service_names_output.extend(
            [f"  {service_name}" for service_name in service.service_names]
        )
        service_names_output.append("")

    service_names_output.extend(
        [
            "You can now try to launch upnp_port_forward.client.setup_port_map()",
            "with required_service_names=(<service name>, ...)",
            "To help this library supports more routers, you can submit new service names",
            "here: https://github.com/ethereum/upnp-port-forward/issues - Thanks !!",
        ]
    )

    logger = logging.getLogger("upnp_port_forward.tools.export")
    logging.basicConfig(level=logging.INFO)
    logger.info("\n".join(service_names_output))


def main() -> None:
    logger = logging.getLogger("upnp_port_forward.tools.export")
    try:
        upnp_service_names_by_device = fetch_add_portmapping_services()
    except NoPortMapServiceFound:
        logger.error("No port mapping services found")
    else:
        output_upnp_service_names(upnp_service_names_by_device)


if __name__ == "__main__":
    main()
