API
===

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
    

.. automodule:: upnp_port_forward
    :members:
    :undoc-members:
    :show-inheritance:
