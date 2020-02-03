import json

import pytest

from pyairmore.request.messaging import (
    ChatHistoryRequest,
    MessageHistoryRequest,
    SendMessageRequest,
)


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


@pytest.fixture
def _chat_history_request(airmore_request_factory):
    return airmore_request_factory(ChatHistoryRequest, "foo", 5, 15)


@pytest.fixture
def _chat_history_request_body(_chat_history_request):
    if isinstance(_chat_history_request.body, bytes):
        body = json.loads(_chat_history_request.body.decode("utf-8"))  # type: dict
    else:
        body = json.loads(_chat_history_request.body)  # type: dict

    return body


class TestChatHistoryRequest:
    def test_url_startswith(self, _chat_history_request, airmore_session):
        assert _chat_history_request.url.startswith(airmore_session.base_url)

    def test_url_endswith(self, _chat_history_request):
        assert _chat_history_request.url.endswith("/?Key=MessageGetList")

    def test_method(self, _chat_history_request):
        assert _chat_history_request.method == "POST"

    def test_body_id(self, _chat_history_request_body):
        assert _chat_history_request_body.get("ID") == "foo"

    def test_body_start(self, _chat_history_request_body):
        assert _chat_history_request_body.get("Start") == 5

    def test_body_limit(self, _chat_history_request_body):
        assert _chat_history_request_body.get("Limit") == 15
