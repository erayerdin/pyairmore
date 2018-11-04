# Welcome to PyAirmore

`pyairmore` is an Airmore client library which helps you get information from
and manage your Android device. With PyAirmore, you can:

 - Get detailed information about your device (*)
 - Send, view and manage your messages
 - Manage, add and delete contacts
 - Send and receive files
 - and many more...

 > (*) are the features that it currently has.
 
## License

`pyairmore` is licensed under Apache Software License 2.0. [See the license](../LICENSE.txt).

## Requirements

`pyairmore` requires Python version 3.5 and above to work.

Also, `pyairmore` uses `requests` to handle request-response cycle between
you (client) and Airmore server.

 > #### Tip
 > If you want to develop `pyairmore`, [see development requirements](../dev.requirements.txt).

## Installation

You can use `pip`, `easy_install` or `setup.py` from package to install
`pyairmore`.

### Via `pip`

    pip install pyairmore

### Via `easy_install`

    easy_install pyairmore

### Via `setup.py`

    python setup.py install

## Getting Started

In this basic example, you will learn to get information about your device's
status. First, you need to `import` several things:

```python
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.device import DeviceService
```

Then, you need to initialize an `AirmoreSession` instance.

    ip = IPv4Address("192.168.1.x")  # whatever server's address is
    session = AirmoreSession(ip)  # port is default to 2333

 > #### Warning
 > If you do not know the target device's port, open Airmore application,
 > press the menu button on top-right corner and press "Get IP". You will
 > get your IP and port.

You will need this `session` instance in order to create a `DeviceService`
instance.

    service = DeviceService(session)

Then you can get details about your device:

    details = service.fetch_device_details()
    details.power  # 0.65
    details.brand  # gm

 > #### Warning
 > Make sure the target device is not locked and better has Airmore opened.
 > After you `fetch_device_details`, you will probably to receive an
 > authorization dialog from the target device's Airmore application.

## What's Further

You can check out [services](services/) to see what you can do with Airmore
server.

If you intend to develop, you might also want to see [how sessions work](sessions/),
check *todos* or watch issues.
