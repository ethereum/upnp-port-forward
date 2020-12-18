import logging

import pytest

from upnp_port_forward.tools.export import UPnPServiceNames, output_upnp_service_names


@pytest.fixture
def upnp_service_names():
    upnp_service_name_1 = UPnPServiceNames(
        "Device 1", "Location 1", ("Service 1.1", "Service 1.2")
    )
    upnp_service_name_2 = UPnPServiceNames(
        "Device 2", "Location 2", ("Service 2.1", "Service 2.2")
    )
    return (upnp_service_name_1, upnp_service_name_2)


def test_output_upnp_service_names(upnp_service_names, caplog):
    expected_output = (
        "Device Name:     Device 1\n"
        "Device Location: Location 1\n"
        "Available UPnP services found on this device:\n"
        "  Service 1.1\n"
        "  Service 1.2\n"
        "\n"
        "Device Name:     Device 2\n"
        "Device Location: Location 2\n"
        "Available UPnP services found on this device:\n"
        "  Service 2.1\n"
        "  Service 2.2\n"
    )
    caplog.set_level(logging.INFO)
    output_upnp_service_names(upnp_service_names)
    assert expected_output in caplog.text
