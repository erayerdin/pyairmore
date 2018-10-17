Device Service
==============

Service related to device is under ``pyairmore.services.device`` module. This module contains several services,
processes and objects. The important one that we will heavily use is ``DeviceService`` class.

.. autoclass:: pyairmore.services.device.DeviceService

After you initialize ``AirmoreSession``, you can initialize ``DeviceService`` by passing your session instance to it.

.. code-block:: python

 from pyairmore.services.device import DeviceService

 service = DeviceService(session)  # `session` is your session instance

After you initialize your service, you can do what ``DeviceService`` lets you to do.

Getting Detailed Information About Target Device
------------------------------------------------

You can get detailed information from the target device via ``DeviceService::fetch_device_detail`` method.

.. automethod:: pyairmore.services.device.DeviceService.fetch_device_detail

To get detailed information:

.. code-block:: python

 detail = service.fetch_device_detail()
 print(detail.power)  # 0.74

This method will return ``DeviceDetail`` object. To see what attributes it has, see the source.

.. autoclass:: pyairmore.services.device.DeviceDetail

Taking Screenshot of Target Device
----------------------------------

You can take a screenshot of the target device via ``DeviceService::take_screenshot`` method.

.. automethod:: pyairmore.services.device.DeviceService.take_screenshot

To take a screenshot:

.. code-block:: python

 image = service.take_screenshot()
