class DeviceDetails:
    """A class that contains several attributes which are details about the
    target device. """

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
