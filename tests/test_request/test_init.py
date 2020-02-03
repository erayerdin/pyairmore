from unittest import mock

import pytest
import urllib3.util.url

from pyairmore.request import AirmoreRequest, ApplicationOpenRequest


@pytest.fixture
def _airmore_request(airmore_request_factory):
    return airmore_request_factory(AirmoreRequest)


class TestAirmoreRequest:
    def test_method(self, _airmore_request):
        _airmore_request.prepare_method("get")
        assert _airmore_request.method == "POST"

        _airmore_request.prepare_method("whatever")
        assert _airmore_request.method == "POST"

        _airmore_request.prepare_method("post")
        assert _airmore_request.method == "POST"

    def test_prepare_url_contains_base_url(self, _airmore_request, airmore_session):
        _airmore_request.prepare_url("/foo", {})
        assert (
            airmore_session.base_url
            == _airmore_request.url[: len(airmore_session.base_url)]
        )

    def test_prepare_url_without_params(self, _airmore_request, airmore_session):
        _airmore_request.prepare_url("/foo", {})
        assert _airmore_request.url == airmore_session.base_url + "/foo"

    def test_prepare_url_with_params(self, _airmore_request, airmore_session):
        _airmore_request.prepare_url("/", {"foo": "bar"})
        assert _airmore_request.url == airmore_session.base_url + "/?foo=bar"


@pytest.fixture
def _application_open_request(airmore_request_factory):
    return airmore_request_factory(ApplicationOpenRequest)


class TestApplicationOpenRequest:
    def test_url(self, _application_open_request):
        assert _application_open_request.url.endswith("/?Key=PhoneCheckAuthorization")


@pytest.fixture
def _parsed_session_url(airmore_session):
    return urllib3.util.url.parse_url(airmore_session.base_url)


class TestAirmoreSession:
    @mock.patch("pyairmore.request.socket.socket")
    def test_is_server_running(self, mock_sock, airmore_session):
        mock_sock().connect_ex.return_value = 0
        assert airmore_session.is_server_running
        assert mock_sock.called

    def test_is_application_open(self, airmore_session):
        assert airmore_session.is_application_open

    def test_request_authorization(self, airmore_session):
        assert airmore_session.request_authorization()

    def test_base_url_scheme(self, _parsed_session_url):
        assert _parsed_session_url.scheme == "http"

    def test_base_url_hostname(self, _parsed_session_url):
        # parsed = urllib3.util.url.parse_url(self.session.base_url)
        assert _parsed_session_url.hostname == "127.0.0.1"

    def test_base_url_port(self, _parsed_session_url):
        # parsed = urllib3.util.url.parse_url(self.session.base_url)
        assert _parsed_session_url.port == 2333
