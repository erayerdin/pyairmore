import pytest

from pyairmore.services.device import DeviceService


@pytest.fixture
def _device_service(airmore_session):
    return DeviceService(airmore_session)


@pytest.fixture
def _device_service_fetch_device_details(_device_service):
    return _device_service.fetch_device_details()


class TestDeviceServiceFetchDeviceDetails:
    def test_model(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.model == "GM 5 Plus"

    def test_brand(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.brand == "gm"

    def test_device_name(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.device_name == "My Device"

    def test_phone_number(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.phone_number is None

    def test_imei(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.imei == "whatever"

    def test_imsi(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.imsi == "whatever"

    def test_mac_address(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.mac_address == "02:00:00:00:00:00"

    def test_serial_number(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.serial_number == "whatever"

    def test_device_serial_number(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.device_serial_number == "whatever"

    def test_root(self, _device_service_fetch_device_details):
        assert not _device_service_fetch_device_details.is_root

    def test_sdk_version_id(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.sdk_version_id == 26

    def test_sdk_version_name(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.sdk_version_name == "8.0.0"

    def test_platform(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.platform == 1

    def test_app_version_code(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.app_version_code == 61

    def test_app_version_name(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.app_version_name == "1.6.1"

    def test_wifi(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.is_wifi_on

    def test_external_sd_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.external_sd_total_size == 0

    def test_external_sd_available_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.external_sd_available_size == 0

    def test_internal_sd_total_size(self, _device_service_fetch_device_details):
        assert (
            _device_service_fetch_device_details.internal_sd_total_size == 27955458048
        )

    def test_internal_sd_available_size(self, _device_service_fetch_device_details):
        assert (
            _device_service_fetch_device_details.internal_sdv_available_size
            == 9449390080
        )

    def test_memory_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.memory_total_size == 27955458048

    def test_memory_available_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.memory_available_size == 9449390080

    def test_call_history_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.call_history_count == 343

    def test_contact_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.contacts_count == 180

    def test_message_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.messages_count == 104

    def test_pictures_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.pictures_count == 2144

    def test_pictures_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.pictures_total_size == 575796564

    def test_songs_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.songs_count == 1031

    def test_songs_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.songs_total_size == 8438843206

    def test_videos_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.videos_count == 7

    def test_videos_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.videos_total_size == 1078229335

    def test_apks_total_size(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.apks_total_size == 1845013784

    def test_user_apks_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.user_apks_count == 70

    def test_system_apks_count(self, _device_service_fetch_device_details):
        assert _device_service_fetch_device_details.system_apks_count == 152

    def test_resolution(self, _device_service_fetch_device_details):
        resolution = _device_service_fetch_device_details.resolution
        assert resolution[0] == 1080
        assert resolution[1] == 1920

    def test_power(self, _device_service_fetch_device_details):
        power = _device_service_fetch_device_details.power
        assert power == 0.85


def test_device_service_take_screenshot(_device_service):
    ss = _device_service.take_screenshot()
    assert ss is not None
