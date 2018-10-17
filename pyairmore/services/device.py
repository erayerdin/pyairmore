"""This module contains DeviceService which helps you get detail about target device.

To use DeviceService::take_screenshot, you need to install ``pillow``.
"""

import warnings

from pyairmore.services import Service

try:
    import PIL
    import PIL.Image
except ImportError:
    warnings.warn("In order to use DeviceService::take_screenshot, you will need 'pillow' module to be installed.",
                  ImportWarning)

import typing

import pyairmore.request
import pyairmore.services


class DeviceDetail:
    """A class that contains several attributes which are details about the target device.

    This class is to be initialized by DeviceService.
    """
    def __init__(self):
        self.model = None  # type: str
        self.brand = None  # type: str
        self.device_name = None  # type: str
        # phone_number might be "" from airmore server
        self.phone_number = None  # type: str
        self.imei = None  # type: str
        self.imsi = None  # type: str
        self.mac_address = None  # type: str
        self.serial_number = None  # type: str
        self.device_serial_number = None  # type: str
        self.power = 0.0  # type: float
        self.resolution = (0, 0)  # type: typing.Tuple[int]
        self.is_root = False  # type: bool
        self.sdk_version_id = 0  # type: int
        self.sdk_version_name = None  # type: str
        self.platform = 1  # type: int
        self.app_version_code = 1  # type: int
        self.app_version_name = None  # type:str
        self.is_wifi_on = True  # type: bool
        # all in bytes
        self.external_sd_total_size = 0  # type: int
        self.external_sd_available_size = 0  # type: int
        self.internal_sd_total_size = 0  # type: int
        self.internal_sdv_available_size = 0  # type: int
        self.memory_total_size = 0  # type: int
        self.memory_available_size = 0  # type: int
        self.call_history_count = 0  # type: int
        self.contacts_count = 0  # type: int
        self.messages_count = 0  # type: int
        self.pictures_count = 0  # type: int
        self.pictures_total_size = 0  # type: int
        self.songs_count = 0  # type: int
        self.songs_total_size = 0  # type: int
        self.videos_count = 0  # type: int
        self.videos_total_size = 0  # type: int
        self.apks_total_size = 0  # type: int
        self.system_apks_count = 0  # type: int
        self.user_apks_count = 0  # type: int

#############
# Processes #
#############


class DeviceDetailProcess(pyairmore.services.Process):
    """A process to get device detail.

     | **Endpoint:** /?Key=PhoneGetDeviceInfo&IsDetail=true
     | **Method:** POST
    """

    def __init__(self, service: pyairmore.services.Service):
        super().__init__(service)

        self.url = "/?Key=PhoneGetDeviceInfo&IsDetail=true"
        self.method = "POST"


class DeviceScreenshotProcess(pyairmore.services.Process):
    """A process to get device detail.

     | **Endpoint:** /?Key=PhoneRefreshScreen
     | **Method:** POST
    """

    def __init__(self, service: Service):
        super().__init__(service)

        self.url = "/?Key=PhoneRefreshScreen"
        self.method = "POST"


############
# Services #
############


class DeviceService(pyairmore.services.Service):
    """A service to get details about the target device."""

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

    def fetch_device_detail(self) -> DeviceDetail:
        """Fetches detail about the target device.

        :return: Detail about the target device.
        """
        response = self.request(DeviceDetailProcess)
        data = response.json()  # type: dict
        detail = DeviceDetail()

        detail.model = data.get("Model", None)
        detail.brand = data.get("Brand", None)
        detail.device_name = data.get("DeviceName", None)
        # if PhoneNumber is "", then stay None
        detail.phone_number = None if data.get("PhoneNumber", None) == "" else data.get("PhoneNumber", None)
        detail.imei = data.get("IMEI", None)
        detail.imsi = data.get("IMSI", None)
        detail.mac_address = data.get("MAC", None)
        detail.serial_number = data.get("SerialNum", None)
        detail.device_serial_number = data.get("DeviceSN", None)
        detail.power = data.get("Power", 0.0) / 100

        # resolution parsing
        if "*" in data.get("Resolution", ""):
            detail.resolution = tuple(map(int, data.get("Resolution").split("*", 1)))

        detail.is_root = False if data.get("Root", None) == 0 else True
        detail.sdk_version_id = data.get("SDKVersionID", 1)
        detail.sdk_version_name = data.get("SDKVersionName", None)
        detail.platform = data.get("Platform", 1)
        detail.app_version_code = data.get("AppVersionCode", 1)
        detail.app_version_name = data.get("AppVersionName", None)
        detail.is_wifi_on = False if data.get("Wifi", None) == 0 else True
        detail.external_sd_total_size = data.get("ExtSDSize", 0)
        detail.external_sd_available_size = data.get("ExtSDAvaSize", 0)
        detail.internal_sd_total_size = data.get("SDSize", 0)
        detail.internal_sdv_available_size = data.get("SDVAvaSize", 0)
        detail.memory_available_size = data.get("MemoryAvaSize", 0)
        detail.memory_total_size = data.get("MemorySize", 0)
        detail.call_history_count = data.get("CallHistoryCount", 0)
        detail.contacts_count = data.get("ContactCount", 0)
        detail.messages_count = data.get("MsgCount", 0)
        detail.pictures_count = data.get("PicCount", 0)
        detail.pictures_total_size = data.get("PicSize", 0)
        detail.songs_count = data.get("MusicCount", 0)
        detail.songs_total_size = data.get("MusicSize", 0)
        detail.videos_count = data.get("VideoCount", 0)
        detail.videos_total_size = data.get("VideoSize", 0)
        detail.apks_total_size = data.get("APKSize", 0)
        detail.system_apks_count = data.get("SystemApkCount", 0)
        detail.user_apks_count = data.get("UserApkCount", 0)

        return detail

    def take_screenshot(self) -> PIL.Image.Image:
        """Takes screenshot of the target device.

        This method relies on ``pillow`` package. You need to install it.

        :return: Screenshot.
        """

        response = self.request(DeviceScreenshotProcess)
        content = response.text

        from io import BytesIO
        import base64
        from pyairmore import _clean_base64_png

        content = _clean_base64_png(content)
        image = PIL.Image.open(BytesIO(base64.b64decode(content)))

        return image
