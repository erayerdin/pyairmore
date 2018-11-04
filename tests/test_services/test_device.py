import collections
import ipaddress
import unittest

import pyairmore.request
import pyairmore.services.device


class DeviceDetailRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.device.DeviceService(cls.session)

    def setUp(self):
        self.detail = self.service.fetch_device_details()

    def test_model(self):
        self.assertEqual(self.detail.model, "GM 5 Plus")

    def test_brand(self):
        self.assertEqual(self.detail.brand, "gm")

    def test_device_name(self):
        self.assertEqual(self.detail.device_name, "My Device")

    def test_phone_number(self):
        self.assertIsNone(self.detail.phone_number)

    def test_imei(self):
        self.assertEqual(self.detail.imei, "whatever")

    def test_imsi(self):
        self.assertEqual(self.detail.imsi, "whatever")

    def test_mac_address(self):
        self.assertEqual(self.detail.mac_address, "02:00:00:00:00:00")

    def test_serial_number(self):
        self.assertEqual(self.detail.serial_number, "whatever")

    def test_device_serial_number(self):
        self.assertEqual(self.detail.device_serial_number, "whatever")

    def test_root(self):
        self.assertFalse(self.detail.is_root)

    def test_sdk_version_id(self):
        self.assertEqual(self.detail.sdk_version_id, 26)

    def test_sdk_version_name(self):
        self.assertEqual(self.detail.sdk_version_name, "8.0.0")

    def test_platform(self):
        self.assertEqual(self.detail.platform, 1)

    def test_app_version_code(self):
        self.assertEqual(self.detail.app_version_code, 61)

    def test_app_version_name(self):
        self.assertEqual(self.detail.app_version_name, "1.6.1")

    def test_wifi(self):
        self.assertTrue(self.detail.is_wifi_on)

    def test_external_sd_total_size(self):
        self.assertEqual(self.detail.external_sd_total_size, 0)

    def test_external_sd_available_size(self):
        self.assertEqual(self.detail.external_sd_available_size, 0)

    def test_internal_sd_total_size(self):
        self.assertEqual(self.detail.internal_sd_total_size, 27955458048)

    def test_internal_sd_available_size(self):
        self.assertEqual(self.detail.internal_sdv_available_size, 9449390080)

    def test_memory_total_size(self):
        self.assertEqual(self.detail.memory_total_size, 27955458048)

    def test_memory_available_size(self):
        self.assertEqual(self.detail.memory_available_size, 9449390080)

    def test_call_history_count(self):
        self.assertEqual(self.detail.call_history_count, 343)

    def test_contact_count(self):
        self.assertEqual(self.detail.contacts_count, 180)

    def test_message_count(self):
        self.assertEqual(self.detail.messages_count, 104)

    def test_pictures_count(self):
        self.assertEqual(self.detail.pictures_count, 2144)

    def test_pictures_total_size(self):
        self.assertEqual(self.detail.pictures_total_size, 575796564)

    def test_songs_count(self):
        self.assertEqual(self.detail.songs_count, 1031)

    def test_songs_total_size(self):
        self.assertEqual(self.detail.songs_total_size, 8438843206)

    def test_videos_count(self):
        self.assertEqual(self.detail.videos_count, 7)

    def test_videos_total_size(self):
        self.assertEqual(self.detail.videos_total_size, 1078229335)

    def test_apks_total_size(self):
        self.assertEqual(self.detail.apks_total_size, 1845013784)

    def test_user_apks_count(self):
        self.assertEqual(self.detail.user_apks_count, 70)

    def test_system_apks_count(self):
        self.assertEqual(self.detail.system_apks_count, 152)

    def test_resolution(self):
        resolution = self.detail.resolution
        self.assertIsInstance(resolution, collections.Iterable)
        self.assertEqual(resolution[0], 1080)
        self.assertEqual(resolution[1], 1920)

    def test_power(self):
        power = self.detail.power
        self.assertIsInstance(power, float)
        self.assertEqual(power, 0.85)


class DeviceScreenshotRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.device.DeviceService(cls.session)

    def test_valid_image(self):
        self.image = self.service.take_screenshot()
        # will fail if not valid image
