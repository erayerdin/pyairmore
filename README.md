# PyAirmore

|             | Build | Coverage |
|-------------|-------|----------|
| master      | [![Travis (.org) master](https://img.shields.io/travis/erayerdin/pyairmore/master.svg?style=flat-square)](travis-ci.org/erayerdin/pyairmore)           | [![Coveralls github master](https://img.shields.io/coveralls/github/erayerdin/pyairmore/master.svg?style=flat-square)](https://coveralls.io/github/erayerdin/pyairmore) |
| development | [![Travis (.org) development](https://img.shields.io/travis/erayerdin/pyairmore/development.svg?style=flat-square)](travis-ci.org/erayerdin/pyairmore) | [![Coveralls github development](https://img.shields.io/coveralls/github/erayerdin/pyairmore/development.svg?style=flat-square)](https://coveralls.io/github/erayerdin/pyairmore) |

PyAirmore is a Airmore client library for Android Airmore server. You can get
information from Airmore server on your Android.

# Simple Example

At first, you need to know your device's IPv4 address, which you can easily
find out by simply opening your Airmore application on Android, click options
(top-right, triple vertical dots) button, press "Get IP".

Then, you start coding:

    from ipaddress import IPv4Address
    from pyairmore.request import AirmoreSession  # import session
    
    device_ip = IPv4Address("your ip address")  # need to put your ip
    session = AirmoreSession(device_ip)  # also you can put your port as int
    # airmore's port default is 2333
    
    # you can check if your airmore server is running
    # you better do it before doing anything on your device
    session.is_server_running  # True
    
    # and before doing anything, you must request access from your device
    # you better turn on your airmore app on your device and watch it
    session.request_authorization()  # True if accepted, False if denied
    # when you request authorization, airmore app on your device will
    # provide a dialogue to accept the authorization, ensure to accept
    
Now that we created an authorized session, we can  now create a `Service`.
You can use services to access many functionalities of your device. For the
sake of simplicity, we will use a service called `DeviceService`.

    # assuming we have done above
    
    from pyairmore.service.device import DeviceService
    
    device = DeviceService(session)
    # all services initializes with a session instance
    
    # you can once more do `Session::is_server_running` and
    # `Session::request_authorization` just in case
    
    device.fetch_device_detail()
    
    # Now we can access many details about out device.
    
    device.power  # 0.74
    device.device_name  # "My device"
    device.is_root  # True, bcoz real men use rooted device
    device.imei  # muhahaha
    device.call_history_count  # 666
    
    # so on and so forth
