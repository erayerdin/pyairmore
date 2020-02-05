from pytest_httpserver import HTTPServer


def test_screenshot(httpserver: HTTPServer, device_service):
    with open("resources/test/screenshot.txt", "rb") as f:
        httpserver.expect_request(
            "/", "POST", query_string={"Key": "PhoneRefreshScreen"}
        ).respond_with_data(f.read())

    assert device_service.take_screenshot()  # will not fail
