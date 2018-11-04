"""PyAirmore (the package name of which is ``pyairmore``) is a Python client
library for Android Airmore server, which helps the developers to take
programmatic actions on Android. """

import pyairmore.request

__version__ = "0.1.1a2"
__author__ = "Eray Erdin"


def _clean_base64_png(encoded: str) -> str:
    return encoded[22:]
