# PyAirmore

[![PyPI](https://img.shields.io/pypi/v/pyairmore.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/pyairmore/)
[![PyPI - Status](https://img.shields.io/pypi/status/pyairmore.svg?style=flat-square)](https://pypi.org/project/pyairmore/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyairmore.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/pyairmore/)
[![PyPI - License](https://img.shields.io/pypi/l/pyairmore.svg?style=flat-square)](LICENSE.txt)
[![Codacy grade](https://img.shields.io/codacy/grade/f9dcb968a7cc4804b64ae7e0fac3a5be.svg?logo=codacy&logoColor=white&style=flat-square)](https://www.codacy.com/app/erayerdin/pyairmore?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=erayerdin/pyairmore&amp;utm_campaign=Badge_Grade)
[![Telegram](https://img.shields.io/badge/telegram-%40erayerdin-%2332afed.svg?style=flat-square&logo=telegram&logoColor=white)](https://t.me/erayerdin)

|             | Build | Coverage |
|-------------|-------|----------|
| master      | [![Travis (.org) master](https://img.shields.io/travis/erayerdin/pyairmore/master.svg?style=flat-square&logo=travis&logoColor=white)](https://travis-ci.org/erayerdin/pyairmore)           | [![Codecov master](https://img.shields.io/codecov/c/github/erayerdin/pyairmore/master.svg?style=flat-square&logo=codecov&logoColor=white)](https://codecov.io/gh/erayerdin/pyairmore)      |
| development | [![Travis (.org) development](https://img.shields.io/travis/erayerdin/pyairmore/development.svg?style=flat-square&logo=travis&logoColor=white)](https://travis-ci.org/erayerdin/pyairmore) | [![Codecov development](https://img.shields.io/codecov/c/github/erayerdin/pyairmore/development.svg?style=flat-square&logo=codecov&logoColor=white)](https://codecov.io/gh/erayerdin/pyairmore) |

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

    details = device.fetch_device_details()

    # Now we can access many details about out device.

    details.power  # 0.74
    details.device_name  # "My device"
    details.is_root  # True, bcoz real men use rooted device
    details.imei  # muhahaha
    details.call_history_count  # 666

    # so on and so forth

# Documentation

You can get latest documentation from [here](https://pyairmore.readthedocs.io/)
and you can also check out `development` branch's documentation [here](https://pyairmore.readthedocs.io/en/development/),
which is supposed to have next release features.

# Contribution

Please refer to [contribution guide](CONTRIBUTING.md) before contributing.

You can, then, quickly contribute by cloning the project, opening it up with
your favorite IDE or text editor which supports TODOs and check todos for
needs, or you can also check the issues.
