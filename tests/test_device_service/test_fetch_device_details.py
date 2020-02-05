import pytest
from pytest_httpserver import HTTPServer


@pytest.fixture
def _device_details(httpserver: HTTPServer, device_service):
    with open("resources/test/device_detail.json", "rb") as f:
        httpserver.expect_request(
            "/", "POST", query_string={"Key": "PhoneGetDeviceInfo", "IsDetail": "true"}
        ).respond_with_data(f.read())

    return device_service.fetch_device_details()


def test_attrs(_device_details):
    assert _device_details.model == "GM 5 Plus"
    assert _device_details.brand == "gm"
    assert _device_details.device_name == "My Device"
    assert _device_details.phone_number is None
    assert _device_details.imei == "whatever"
    assert _device_details.imsi == "whatever"
    assert _device_details.mac_address == "02:00:00:00:00:00"
    assert _device_details.serial_number == "whatever"
    assert _device_details.device_serial_number == "whatever"
    assert _device_details.power == 0.85
    assert _device_details.resolution == (1080, 1920)
    assert not _device_details.is_root
    assert _device_details.sdk_version_id == 26
    assert _device_details.sdk_version_name == "8.0.0"
    assert _device_details.platform == 1
    assert _device_details.app_version_code == 61
    assert _device_details.app_version_name == "1.6.1"
    assert _device_details.is_wifi_on
    assert _device_details.external_sd_total_size == 0
    assert _device_details.external_sd_available_size == 0
    assert _device_details.internal_sd_total_size == 27955458048
    assert _device_details.internal_sdv_available_size == 9449390080
    assert _device_details.memory_total_size == 27955458048
    assert _device_details.memory_available_size == 9449390080
    assert _device_details.call_history_count == 343
    assert _device_details.contacts_count == 180
    assert _device_details.pictures_count == 2144
    assert _device_details.pictures_total_size == 575796564
    assert _device_details.songs_count == 1031
    assert _device_details.songs_total_size == 8438843206
    assert _device_details.videos_count == 7
    assert _device_details.videos_total_size == 1078229335
    assert _device_details.apks_total_size == 1845013784
    assert _device_details.system_apks_count == 152
    assert _device_details.user_apks_count == 70
