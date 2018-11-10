"""PyAirmore (the package name of which is ``pyairmore``) is a Python client
library for Android Airmore server, which helps the developers to take
programmatic actions on Android. """

__version__ = "0.2.0a1"
__author__ = "Eray Erdin"


def _clean_base64_png(encoded: str) -> str:
    return encoded[22:]
