import pytest
from pytest_httpserver import HTTPServer

import pyairmore.request


@pytest.fixture
def airmore_session():
    from ipaddress import IPv4Address

    return pyairmore.request.AirmoreSession(IPv4Address("127.0.0.1"))


@pytest.fixture
def authorization_required(httpserver: HTTPServer):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneRequestAuthorization"}
    ).respond_with_data("true")
