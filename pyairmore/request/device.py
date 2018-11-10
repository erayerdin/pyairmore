"""Contains ``AirmoreRequest`` classes for device aspect."""
import pyairmore.request


class DeviceDetailsRequest(pyairmore.request.AirmoreRequest):
    """A request to get device detail.

     | **Endpoint:** /?Key=PhoneGetDeviceInfo&IsDetail=true
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

        self.prepare_url("/", {
            "Key": "PhoneGetDeviceInfo",
            "IsDetail": "true"
        })


class DeviceScreenshotRequest(pyairmore.request.AirmoreRequest):
    """A request to get device detail.

     | **Endpoint:** /?Key=PhoneRefreshScreen
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

        self.prepare_url("/", {"Key": "PhoneRefreshScreen"})
