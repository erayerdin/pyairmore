Session
=======

``AirmoreSession`` object is the heart of your application.

.. autoclass:: pyairmore.request.AirmoreSession

It simply extends the ``requests.Session`` class in order to manage requests through the target device.

 - It manages the check of server.
 - It manages the authorization process, both checking and requesting it.
 - It manages URLs, providing consistent URLs for requests to the server.

However, it is heavily managed by ``Service`` objects. While understanding what session is is optional, it will give you
a grasp of how it works if you want to extend the core library's functionality.

To initialize, you will provide a ``ipaddress.IPv4Address`` object and optionally a port as an ``int``. How you will
get these is discussed in the :ref:`Starting A Session` section. After you learn the target device's IP and port,
you can simply:

.. code-block:: python

 from ipaddress import IPv4Address
 from pyairmore.request import AirmoreSession

 ip = IPv4Address("target ip address")  # to validate ip's form
 session = AirmoreSession(ip)

By default, Airmore uses ``2333`` port on target device, so does ``AirmoreSession`` object. If the port is different,
you can pass the port as ``int``.

.. code-block:: python

 session = AirmoreSession(ip, 2334)

.. note::

    Remember! All aspects covered in subsections are already managed by ``Service`` objects. However, these might be
    needed if you intend to contribute to the main project, or simply extend a functionality that you have not found in
    the core library.

Is Server Running?
------------------

Airmore is occasionally inconsistent with its server, either for its own reasons or because of the architecture of
Android.

 - When a device boots, you need to open Airmore manually at least once.
 - Airmore server might shut down automatically when the device is sleeping/idle.
 - Airmore server might shut down automatically when the device's power is low.

So you might need to check if the server is running before each request you are making to the server. An
``AirmoreSession`` instance has a property called ``is_server_running``.

.. automethod:: pyairmore.request.AirmoreSession.is_server_running

.. code-block:: python

 session.is_server_running  # True

This will return boolean ``True`` value if the server is up and running.

.. note::

    ``is_server_running`` is the only method in ``AirmoreSession`` that uses built-in ``socket`` library instead of
    ``requests`` library.

Is Session Authorized?
----------------------

The server is up, but that does not mean that you can do anything with it. Airmore needs authorization for further
processing. The authorization is, as well, not very consistent.
