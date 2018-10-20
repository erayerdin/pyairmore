Starting A Session
==================

There are three steps (last two of which are optional) to start a connection with your Airmore server and ensure it is
working properly:

i. You need to check if Airmore server is present and accepting connections.
ii. You need to check if you are authorized.
iii. You need to request authorization (which requires manual accepting from device).

Usually, all these steps are managed by ``Service`` objects and you do not really need to manage these steps by hand.
To get further information about how ``AirmoreSession`` object works, refer :ref:`Session`.

To begin, you need to acquire an ``AirmoreSession`` class.

.. code-block:: python

 from pyairmore.request import AirmoreSession
 from ipaddress import IPv4Address  # for a valid IP address

 ip = IPv4Address("target ip address")
 session = AirmoreSession(ip)

.. note::

    You can also pass a port number as ``int``. Default is ``2333``.

If you do not know the target device's IP address and/or port, simply open Airmore on target device.

.. figure:: /_static/media/airmore-getip-01.jpg
    :alt: airmore top right menu
    :scale: 50%

    Press the menu on top right and press "Get IP".

.. figure:: /_static/media/airmore-getip-02.jpg
    :alt: airmore ip port
    :scale: 50%

    Note your IP and port.
