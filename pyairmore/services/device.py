"""Services related to device aspect."""

import pyairmore.services
import pyairmore.request
import pyairmore.request.device
import pyairmore.data.device


class DeviceService(pyairmore.services.Service):
    """A service to get details about the target device."""

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

    def fetch_device_details(self) -> pyairmore.data.device.DeviceDetails:
        """Fetches detail about the target device.

        :return: Detail about the target device.
        """
        request = pyairmore.request.device.DeviceDetailsRequest(self.session)
        response = self.session.send(request)
        data = response.json()  # type: dict
        detail = pyairmore.data.device.DeviceDetails()

        detail.model = data.get("Model", None)
        detail.brand = data.get("Brand", None)
        detail.device_name = data.get("DeviceName", None)
        # if PhoneNumber is "", then stay None
        detail.phone_number = None if data.get("PhoneNumber", None) == "" \
            else data.get("PhoneNumber", None)
        detail.imei = data.get("IMEI", None)
        detail.imsi = data.get("IMSI", None)
        detail.mac_address = data.get("MAC", None)
        detail.serial_number = data.get("SerialNum", None)
        detail.device_serial_number = data.get("DeviceSN", None)
        detail.power = data.get("Power", 0.0) / 100

        # resolution parsing
        if "*" in data.get("Resolution", ""):
            detail.resolution = tuple(map(int, data.get("Resolution")
                                          .split("*", 1)))

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

    # noinspection PyUnresolvedReferences
    def take_screenshot(self) -> "PIL.Image.Image":
        """Takes screenshot of the target device.

        This method relies on ``pillow`` package. You need to install it.

        :return: Screenshot.
        """
        import PIL.Image

        request = pyairmore.request.device.DeviceScreenshotRequest(
            self.session
        )
        response = self.session.send(request)
        content = response.text

        from io import BytesIO
        import base64
        from pyairmore import _clean_base64_png

        content = _clean_base64_png(content)
        image = PIL.Image.open(BytesIO(base64.b64decode(content)))

        return image
