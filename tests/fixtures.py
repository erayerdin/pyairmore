import pytest
from pytest_httpserver import HTTPServer

import pyairmore.request
import pyairmore.services.device
import pyairmore.services.messaging


@pytest.fixture
def airmore_session():
    from ipaddress import IPv4Address

    return pyairmore.request.AirmoreSession(IPv4Address("127.0.0.1"))


@pytest.fixture
def device_service(airmore_session, authorization_required):
    return pyairmore.services.device.DeviceService(airmore_session)


@pytest.fixture
def messaging_service(airmore_session, authorization_required):
    return pyairmore.services.messaging.MessagingService(airmore_session)


@pytest.fixture
def authorization_required(httpserver: HTTPServer):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneRequestAuthorization"}
    ).respond_with_data("true")


@pytest.fixture
def httpserver_listen_address():
    return ("localhost", 2333)
