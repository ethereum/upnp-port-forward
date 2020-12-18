API
===

Setting up UpnP port forwarding
-------------------------------

This library exposes a simple interface for setting up UPnP port forwarding.

.. code-block:: python

    from upnp_port_forward import setup_port_map, PortMapFailed

    port = 12345
    try:
        internal_ip, external_ip = setup_port_map(port)
    except PortMapFailed:
        ...  # Unable to setup port forwarding
    else:
        print(
            f"Port forwarding setup successfully!  internal_ip={internal_ip}  "
            f"external_ip={external_ip}"
        )
    

If one or several service names allowing port mapping are known (see below: `Exporting port mapping services`_), the library can be forced to use them:

.. code-block:: python

        internal_ip, external_ip = setup_port_map(port, required_service_names=("service name 1", "service name 2",))



Exporting port mapping services
-------------------------------

The export module provides a simple way to get the available UPnP service names allowing port mapping.

.. code-block:: sh

    python upnp_port_forward/tools/export.py

or

.. code-block:: sh

    python -m upnp_port_forward.tools.export


.. automodule:: upnp_port_forward
    :members:
    :undoc-members:
    :show-inheritance:
