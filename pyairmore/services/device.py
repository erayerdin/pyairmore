# todo 1 - package doc

import typing

import pyairmore.request
import pyairmore.services


class DeviceDetailProcess(pyairmore.services.Process):
    # todo 1 - class doc

    def __init__(self, service: pyairmore.services.Service):
        super().__init__(service)

        self.url = "/?Key=PhoneGetDeviceInfo&IsDetail=true"
        self.method = "POST"


class DeviceService(pyairmore.services.Service):
    # todo 1 - class doc
    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

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

    def fetch_device_detail(self):
        self.request(DeviceDetailProcess)
        data = self._response.json()  # type: dict

        self.model = data.get("Model", None)
        self.brand = data.get("Brand", None)
        self.device_name = data.get("DeviceName", None)
        # if PhoneNumber is "", then stay None
        self.phone_number = None if data.get("PhoneNumber", None) == "" else data.get("PhoneNumber", None)
        self.imei = data.get("IMEI", None)
        self.imsi = data.get("IMSI", None)
        self.mac_address = data.get("MAC", None)
        self.serial_number = data.get("SerialNum", None)
        self.device_serial_number = data.get("DeviceSN", None)
        self.power = data.get("Power", 0.0) / 100

        # resolution parsing
        if "*" in data.get("Resolution", ""):
            self.resolution = tuple(map(lambda x: int(x), data.get("Resolution").split("*", 1)))

        self.is_root = False if data.get("Root", None) == 0 else True
        self.sdk_version_id = data.get("SDKVersionID", 1)
        self.sdk_version_name = data.get("SDKVersionName", None)
        self.platform = data.get("Platform", 1)
        self.app_version_code = data.get("AppVersionCode", 1)
        self.app_version_name = data.get("AppVersionName", None)
        self.is_wifi_on = False if data.get("Wifi", None) == 0 else True
        self.external_sd_total_size = data.get("ExtSDSize", 0)
        self.external_sd_available_size = data.get("ExtSDAvaSize", 0)
        self.internal_sd_total_size = data.get("SDSize", 0)
        self.internal_sdv_available_size = data.get("SDVAvaSize", 0)
        self.memory_available_size = data.get("MemoryAvaSize", 0)
        self.memory_total_size = data.get("MemorySize", 0)
        self.call_history_count = data.get("CallHistoryCount", 0)
        self.contacts_count = data.get("ContactCount", 0)
        self.messages_count = data.get("MsgCount", 0)
        self.pictures_count = data.get("PicCount", 0)
        self.pictures_total_size = data.get("PicSize", 0)
        self.songs_count = data.get("MusicCount", 0)
        self.songs_total_size = data.get("MusicSize", 0)
        self.videos_count = data.get("VideoCount", 0)
        self.videos_total_size = data.get("VideoSize", 0)
        self.apks_total_size = data.get("APKSize", 0)
        self.system_apks_count = data.get("SystemApkCount", 0)
        self.user_apks_count = data.get("UserApkCount", 0)
