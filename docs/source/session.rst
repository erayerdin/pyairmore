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

    Remember! All aspects except `is_application_open` covered in subsections are already managed by ``Service`` objects.
    However, these might be needed if you intend to contribute to the main project, or simply extend a functionality
    that you have not found in the core library.

Is Server Running?
------------------

Airmore is occasionally inconsistent with its server, either for its own reasons or because of the architecture of
Android.

 - When a device boots, you need to open Airmore manually at least once.
 - Airmore server might shut down automatically when the device is sleeping/idle.
 - Airmore server might shut down automatically when the device's power is low.

However, there's one consistent way to see if the server is running. If the server is running, you will see a cloud
icon in notification indicator area (very top of the device) and a persistent notification (which is unremovable) by
Airmore that says "Tap to enter".

.. figure:: /_static/media/airmore-server-running-notification.jpg
    :alt: airmore server running notification
    :scale: 50%

    Airmore server is running.

You can also programmatically check if the server is running via ``AirmoreSession::is_server_running`` property.

.. automethod:: pyairmore.request.AirmoreSession.is_server_running

.. code-block:: python

 session.is_server_running  # True

This will return boolean ``True`` value if the server is up and running.

.. note::

    ``is_server_running`` is the only method in ``AirmoreSession`` that uses built-in ``socket`` library instead of
    ``requests`` library.

.. warning::

    All the aspects from here on assumes that ``is_server_running`` is True. So, this method is an initial step before
    doing any session operations.

Is Application Open?
----------------------

In some occasions, you might need to know if the target device has opened the application and the user can see Airmore
application.

.. automethod:: pyairmore.request.AirmoreSession.is_application_open

You can simply do:

.. code-block:: python

 session.is_application_open  # True

This method will return boolean ``True`` value if the user can now see Airmore application on front.

.. note::

    This method is not used in ``Service`` classes for validation of any kind. It only gives information about if the
    user on target device can see Airmore main activity.

Requesting Authorization
------------------------

To do anything with device, you need to request authorization first and the target device must accept it. The default
timeout on target device is 30 seconds. So, after 30 seconds, your request will be rejected automatically.

To request authorization, you use ``AirmoreSession::request_authorization`` method.

.. automethod:: pyairmore.request.AirmoreSession.request_authorization

To request authorization from the target device:

.. code-block:: python

 session.request_authorization()  # True

This will show up a dialog to accept the authorization request on the device.

There are some key behaviors about this method:

 - When the target device is sleeping or in lock screen, you will need to unlock it
   (if it is protected by password or PIN) to accept authorization.
 - You can request authorization anywhere. You do not need to open up Airmore.
 - This method will return boolean ``True`` value if the authorization has already been accepted.

.. warning::

    This method will block the current thread until it has a response.

.. warning::

    On some devices, when you request authorization when the screen is locked, and you unlock the device, the whole
    launcher might freeze, dialog might not even show up and the launcher activity might not even accept any touch
    event. In this case, show your recent application list and clear "Airmore".

.. note::

    Since ``AirmoreSession::request_authorization`` method returns ``True`` even if the authorization is accepted, you
    can use it before every request for a safety measure, to ensure if you are authorized. ``Service`` classes already
    use this method.
