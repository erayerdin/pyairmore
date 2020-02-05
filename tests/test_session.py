import ipaddress

import pytest
from pytest_httpserver import HTTPServer

from pyairmore.request import (
    AirmoreSession,
    AuthorizationException,
    ServerUnreachableException,
)


def test_is_server_running(httpserver, airmore_session):
    assert airmore_session.is_server_running


def test_is_application_open_zero(
    httpserver: HTTPServer, authorization_required, airmore_session
):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneCheckAuthorization"}
    ).respond_with_data('"0"')
    assert airmore_session.is_application_open


def test_is_application_open_one(
    httpserver: HTTPServer, authorization_required, airmore_session
):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneCheckAuthorization"}
    ).respond_with_data('"1"')
    assert not airmore_session.is_application_open


def test_is_application_open_invalid_status(
    httpserver: HTTPServer, authorization_required, airmore_session
):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneCheckAuthorization"}
    ).respond_with_data('"1"', status=400)
    assert not airmore_session.is_application_open


def test_server_unreachable():
    session = AirmoreSession(ipaddress.IPv4Address("127.0.0.1"), 8080)
    with pytest.raises(ServerUnreachableException):
        session.is_application_open


def test_authorization_required(httpserver: HTTPServer, airmore_session):
    with pytest.raises(AuthorizationException):
        airmore_session.is_application_open
