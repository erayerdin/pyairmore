import ipaddress
import json
import unittest

import pytest

import pyairmore.request
from pyairmore.request.messaging import MessageHistoryRequest, SendMessageRequest


@pytest.fixture
def _message_history_request(airmore_request_factory):
    return airmore_request_factory(MessageHistoryRequest)


class TestMessageHistoryRequest:
    def test_url_startswith(self, _message_history_request, airmore_session):
        assert _message_history_request.url.startswith(airmore_session.base_url)

    def test_url_endswith(self, _message_history_request):
        assert _message_history_request.url.endswith("/?Key=MessageGetLatest")

    def test_method(self, _message_history_request):
        assert _message_history_request.method == "POST"


@pytest.fixture
def _send_message_request(airmore_request_factory):
    return airmore_request_factory(SendMessageRequest, "321", "foo")


@pytest.fixture
def _send_message_request_body(_send_message_request):
    if isinstance(_send_message_request.body, bytes):
        body = json.loads(_send_message_request.body.decode("utf-8"))[0]  # type: dict
    else:
        body = json.loads(_send_message_request.body)[0]  # type: dict

    return body


class TestSendMessageRequest:
    def test_url_startswith(self, _send_message_request, airmore_session):
        assert _send_message_request.url.startswith(airmore_session.base_url)

    def test_url_endswith(self, _send_message_request):
        assert _send_message_request.url.endswith("/?Key=MessageSend")

    def test_method(self, _send_message_request):
        assert _send_message_request.method == "POST"

    def test_body_phone(self, _send_message_request_body):
        assert _send_message_request_body.get("Phone") == "321"

    def test_body_content(self, _send_message_request_body):
        assert _send_message_request_body.get("Content") == "foo"

    def test_body_uid(self, _send_message_request_body):
        assert isinstance(_send_message_request_body.get("UniqueID"), str)
        assert len(_send_message_request_body.get("UniqueID")) > 0


class ChatHistoryRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.messaging.ChatHistoryRequest(
            cls.session, "foo", 5, 15
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(cls.request.body.decode("utf-8"))  # type: dict
        else:
            cls.body = json.loads(cls.request.body)  # type: dict

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=MessageGetList"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_id(self):
        self.assertEqual(self.body.get("ID"), "foo")

    def test_body_start(self):
        self.assertEqual(self.body.get("Start"), 5)

    def test_body_limit(self):
        self.assertEqual(self.body.get("Limit"), 15)
