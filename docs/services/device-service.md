# Device Service

`DeviceService` provides detailed information about and screenshot of
target device.

To create `DeviceService`, simply do:

    from pyairmore.services.device import DeviceService
    service = DeviceService(session)

## Getting Detailed Information

`fetch_device_details` method will return a `DeviceDetails` instance, which
has many properties stating target device's details. Do as below:

    details = service.fetch_device_details()
    details.power  # 0.65
    details.is_root  # True
    details.resolution  # (1080, 1920) tuple

There are many properties of `DeviceDetails`. Below is the complete table:

| Name | Type | Default | Description |
|------|------|---------|-------------|
| model                       | str        | None   |   |
| brand                       | str        | None   |   |
| device_name                 | str        | None   |   |
| phone_number                | str        | None   |   |
| imei                        | str        | None   |   |
| imsi                        | str        | None   |   |
| mac_address                 | str        | None   |   |
| serial_number               | str        | None   |   |
| device_serial_number        | str        | None   |   |
| power                       | float      | 0.0    | Between 0 and 1. |
| resolution                  | tuple[int] | (0, 0) | y and x, always 2 `int`s |
| is_root                     | bool       | False  |   |
| sdk_version_id              | int        | 0      |   |
| sdk_version_name            | str        | None   |   |
| platform                    | int        | 0      |   |
| app_version_code            | int        | 0      |   |
| app_version_name            | str        | None   |   |
| is_wifi_on                  | bool       | True   |   |
| external_sd_total_size      | int        | 0      |   |
| external_sd_available_size  | int        | 0      |   |
| internal_sd_total_size      | int        | 0      |   |
| internal_sdv_available_size | int        | 0      |   |
| memory_total_size           | int        | 0      |   |
| memory_available_size       | int        | 0      |   |
| call_history_count          | int        | 0      |   |
| contacts_count              | int        | 0      |   |
| messages_count              | int        | 0      |   |
| pictures_count              | int        | 0      |   |
| pictures_total_size         | int        | 0      |   |
| songs_count                 | int        | 0      |   |
| songs_total_size            | int        | 0      |   |
| videos_count                | int        | 0      |   |
| videos_total_size           | int        | 0      |   |
| apks_total_size             | int        | 0      |   |
| system_apks_count           | int        | 0      |   |
| user_apks_count             | int        | 0      |   |

## Taking Screenshot

`take_screenshot` method will return `PIL.Image.Image` instance, which is
the screenshot of target device.

 > #### Warning
 > `pillow` package is not installed while installing `pyairmore` since this
 > functionality is only required in `take_screenshot` method. To use this
 > method without any possible `ImportError`s, install `pillow`.

To get the screenshot of target device:

    image = service.take_screenshot()
    image.show()  # will show you the image

 > #### Warning
 > On some devices, Airmore application's main activity must be kept open,
 > which makes this functionality obsolete.
