import ipaddress
import urllib3.util.url
import unittest
from unittest import mock

import pyairmore.request

from tests import HTTPrettyTestCase
from tests.test_request import AirmoreRequestTestCase


class TestAirmoreRequest:
    @classmethod
    def setup_class(cls):
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )

    def setup_method(self):
        self.request = pyairmore.request.AirmoreRequest(self.session)

    def test_method(self):
        self.request.prepare_method("get")
        assert self.request.method == "POST"

        self.request.prepare_method("whatever")
        assert self.request.method == "POST"

        self.request.prepare_method("post")
        assert self.request.method == "POST"

    def test_prepare_url_contains_base_url(self):
        self.request.prepare_url("/foo", {})
        assert (
            self.session.base_url
            == self.request.url[: len(self.session.base_url)]
        )

    def test_prepare_url_without_params(self):
        self.request.prepare_url("/foo", {})
        assert self.request.url == self.session.base_url + "/foo"

    def test_prepare_url_with_params(self):
        self.request.prepare_url("/", {"foo": "bar"})
        assert self.request.url == self.session.base_url + "/?foo=bar"


class TestApplicationOpenRequest(AirmoreRequestTestCase):
    request_class = pyairmore.request.ApplicationOpenRequest

    def test_url(self):
        assert self.request.url.endswith("/?Key=PhoneCheckAuthorization")


class TestAirmoreSession:
    @classmethod
    def setup_class(cls):
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.parsed = urllib3.util.url.parse_url(cls.session.base_url)

    @mock.patch("pyairmore.request.socket.socket")
    def test_is_server_running(self, mock_sock):
        mock_sock().connect_ex.return_value = 0
        assert self.session.is_server_running
        assert mock_sock.called

    def test_is_application_open(self):
        assert self.session.is_application_open

    def test_request_authorization(self):
        assert self.session.request_authorization()

    def test_base_url_scheme(self):
        assert self.parsed.scheme == "http"

    def test_base_url_hostname(self):
        parsed = urllib3.util.url.parse_url(self.session.base_url)
        assert self.parsed.hostname == "127.0.0.1"

    def test_base_url_port(self):
        parsed = urllib3.util.url.parse_url(self.session.base_url)
        assert self.parsed.port == 2333
