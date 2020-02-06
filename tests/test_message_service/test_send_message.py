import pytest
from pytest_httpserver import HTTPServer

from pyairmore.services.messaging import MessageRequestGSMError


def test_successful(httpserver: HTTPServer, messaging_service):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "MessageSend"}
    ).respond_with_data("2")
    messaging_service.send_message("123", "lorem")  # will not fail


def test_failure(httpserver: HTTPServer, messaging_service):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "MessageSend"}
    ).respond_with_data("1")
    with pytest.raises(MessageRequestGSMError):
        messaging_service.send_message("123", "lorem")
