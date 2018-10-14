Getting Started
===============

Installation
------------

To install ``pyairmore``, you can use ``pip`` like so:

.. code-block:: bash

 pip install pyairmore

Starting A Connection
---------------------

There are two steps to start a connection with your Airmore server:

i. You need to check if Airmore server is present and accepting connections.
ii. You need to request a connection (which requires manual accepting from device).

To achieve these steps, you will need an instance of ``pyairmore.request.AirmoreSession`` and pass an
``ipaddress.IPv4Address`` instance to it.

.. code-block:: python

 from pyairmore.request import AirmoreSession
 from ipaddress import IPv4Address
 session = AirmoreSession(IPv4Address("your ip address"))  # default port is 2333 (as int)

Now we can step further. To achieve (i):

 .. code-block:: python

  session.is_server_running

This will return a boolean ``True`` value if the server is up, running and waiting for authorization requests to accept.
If it is ``True``, then you can proceed with step (ii). However, keep in mind those below:

 - Some devices need Airmore to be run at least one after the boot of device or every 10 minute or so.
 - Some devices even need Airmore to be running on front.

.. todo: 3 - confirm points above

To achieve step (ii):

.. code-block:: python

 session.request_authorization()

Now, your Airmore application will provide a dialog to confirm authorization. If you do not approve the request in 30
seconds, your authorization will be rejected.

.. note::

 Remember this process is thread-blocking, which means it will block the thread until Airmore server responds.

This method will return boolean ``True`` if the connection is accepted by the server, else ``False``.

This is how you form a connection between this client library and an Airmore server.

Getting Device's Info
---------------------

Once you successfully get an accepted session, you can now do further, like getting a detailed information about device.
A detailed information about device can be fetched with help of ``pyairmore.services.device.DeviceService``.
``DeviceService`` is actually a ``Service`` class, which is discussed in its own section. In this section, we will use
it for a quick example.

``DeviceService`` is, like any other ``Service``, initialized by providing a ``AirmoreSession`` instance, like so:

.. code-block:: python

 from pyairmore.services.device import DeviceSession
 device = DeviceService(session)  # it is assumed you have already got an AirmoreSession instance called `session`

Once got, you can use ``DeviceService::fetch_device_detail`` method to fetch details.

.. code-block:: python

 device.fetch_device_detail()

And then you can get information from your device as such:

.. code-block:: python

 device.power  # 0.74
 device.imei  # whatever your imei is
 device.apks_total_size  # total size of all your applications

See `DeviceService`_ for more detailed info.

.. _DeviceService: /services.html#device-service
