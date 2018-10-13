# todo [1] package doc
import typing

import pyairmore


class Device(pyairmore.Refreshable):
    # todo 1 - class doc

    def __init__(self):
        self.model = None  # type: str
        self.battery = 0.0  # type: float
        self.firmware_version = None  # type: str
        self.imei = None  # type: str
        self.mac_address = None  # type: str
        self.device_serial_number = None  # type: str
        self.phone_memory = 0  # type: str
        self.app_size = 0  # type: int
        self.video_count = 0  # type: int
        self.picture_count = 0  # type: int
        self.music_count = 0  # type: int
        self.contact_count = 0  # type: int
        self.phone_number = None  # type: str
        self.resolution = (0, 0)  # type: typing.Tuple[int]
        self.is_wifi_on = True  # type: bool
        self.imsi = None  # type: str
        self.serial_number = None  # type: str
        self.is_rooted = False  # type: bool
        self.memory_left = 0  # type: int
        self.app_count = 0  # type: int
        self.document_count = 0  # type: int
        self.video_size = 0  # type: int
        self.picture_size = 0  # type: int
        self.music_size = 0  # type: int
        self.call_history_count = 0  # type: int


