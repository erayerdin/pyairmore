Getting Device's Info
=====================

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

 detail = device.fetch_device_detail()

And then you can get information from your device as such:

.. code-block:: python

 detail.power  # 0.74
 detail.imei  # whatever your imei is
 detail.apks_total_size  # total size of all your applications

See `DeviceService`_ for more detailed info.

.. _DeviceService: /services/device-service.html
