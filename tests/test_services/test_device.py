import collections

from pyairmore.services.device import DeviceService
from tests.test_request import MockedAirmoreSession

RESPONSE = """
{
  "Model": "GM 5 Plus",
  "Brand": "gm",
  "DeviceName": "My Device",
  "PhoneNumber": "",
  "IMEI": "whatever",
  "IMSI": "whatever",
  "MAC": "02:00:00:00:00:00",
  "SerialNum": "whatever",
  "DeviceSN": "whatever",
  "Power": 85,
  "Resolution": "1080*1920",
  "Root": 0,
  "SDKVersionID": 26,
  "SDKVersionName": "8.0.0",
  "Platform": 1,
  "AppVersionCode": 61,
  "AppVersionName": "1.6.1",
  "Wifi": 1,
  "ExtSDSize": 0,
  "ExtSDAvaSize": 0,
  "SDSize": 27955458048,
  "SDVAvaSize": 9449390080,
  "MemoryAvaSize": 9449390080,
  "MemorySize": 27955458048,
  "CallHistoryCount": 343,
  "ContactCount": 180,
  "MsgCount": 104,
  "PicCount": 2144,
  "PicSize": 575796564,
  "MusicCount": 1031,
  "MusicSize": 8438843206,
  "VideoCount": 7,
  "VideoSize": 1078229335,
  "APKSize": 1845013784,
  "SystemApkCount": 152,
  "UserApkCount": 70
}
""".strip()


class MockedDeviceService(MockedAirmoreSession):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = DeviceService(cls.session)

    @classmethod
    def _mount(cls):
        super()._mount()
        cls.__mount_phone_get_device_info_detailed()

    @classmethod
    def __mount_phone_get_device_info_detailed(cls):
        cls.adapter.register_uri(
            "POST",
            "/?Key=PhoneGetDeviceInfo&IsDetail=true",
            text=RESPONSE
        )


class DeviceServiceTestCase(MockedDeviceService):
    def setUp(self):
        self.service.fetch_device_detail()

    def test_model(self):
        self.assertEqual(self.service.model, "GM 5 Plus")

    def test_brand(self):
        self.assertEqual(self.service.brand, "gm")

    def test_device_name(self):
        self.assertEqual(self.service.device_name, "My Device")

    def test_phone_number(self):
        self.assertIsNone(self.service.phone_number)

    def test_imei(self):
        self.assertEqual(self.service.imei, "whatever")

    def test_imsi(self):
        self.assertEqual(self.service.imsi, "whatever")

    def test_mac_address(self):
        self.assertEqual(self.service.mac_address, "02:00:00:00:00:00")

    def test_serial_number(self):
        self.assertEqual(self.service.serial_number, "whatever")

    def test_device_serial_number(self):
        self.assertEqual(self.service.device_serial_number, "whatever")

    def test_root(self):
        self.assertFalse(self.service.is_root)

    def test_sdk_version_id(self):
        self.assertEqual(self.service.sdk_version_id, 26)

    def test_sdk_version_name(self):
        self.assertEqual(self.service.sdk_version_name, "8.0.0")

    def test_platform(self):
        self.assertEqual(self.service.platform, 1)

    def test_app_version_code(self):
        self.assertEqual(self.service.app_version_code, 61)

    def test_app_version_name(self):
        self.assertEqual(self.service.app_version_name, "1.6.1")

    def test_wifi(self):
        self.assertTrue(self.service.is_wifi_on)

    def test_external_sd_total_size(self):
        self.assertEqual(self.service.external_sd_total_size, 0)

    def test_external_sd_available_size(self):
        self.assertEqual(self.service.external_sd_available_size, 0)

    def test_internal_sd_total_size(self):
        self.assertEqual(self.service.internal_sd_total_size, 27955458048)

    def test_internal_sd_available_size(self):
        self.assertEqual(self.service.internal_sdv_available_size, 9449390080)

    def test_memory_total_size(self):
        self.assertEqual(self.service.memory_total_size, 27955458048)

    def test_memory_available_size(self):
        self.assertEqual(self.service.memory_available_size, 9449390080)

    def test_call_history_count(self):
        self.assertEqual(self.service.call_history_count, 343)

    def test_contact_count(self):
        self.assertEqual(self.service.contacts_count, 180)

    def test_message_count(self):
        self.assertEqual(self.service.messages_count, 104)

    def test_pictures_count(self):
        self.assertEqual(self.service.pictures_count, 2144)

    def test_pictures_total_size(self):
        self.assertEqual(self.service.pictures_total_size, 575796564)

    def test_songs_count(self):
        self.assertEqual(self.service.songs_count, 1031)

    def test_songs_total_size(self):
        self.assertEqual(self.service.songs_total_size, 8438843206)

    def test_videos_count(self):
        self.assertEqual(self.service.videos_count, 7)

    def test_videos_total_size(self):
        self.assertEqual(self.service.videos_total_size, 1078229335)

    def test_apks_total_size(self):
        self.assertEqual(self.service.apks_total_size, 1845013784)

    def test_user_apks_count(self):
        self.assertEqual(self.service.user_apks_count, 70)

    def test_system_apks_count(self):
        self.assertEqual(self.service.system_apks_count, 152)

    def test_resolution(self):
        resolution = self.service.resolution
        self.assertIsInstance(resolution, collections.Iterable)
        self.assertEqual(resolution[0], 1080)
        self.assertEqual(resolution[1], 1920)

    def test_power(self):
        power = self.service.power
        self.assertIsInstance(power, float)
        self.assertEqual(power, 0.85)
