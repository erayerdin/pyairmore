import pytest
from pytest_httpserver import HTTPServer


@pytest.fixture
def _message_history(httpserver: HTTPServer, messaging_service):
    with open("resources/test/message_get_latest.json", "rb") as f:
        httpserver.expect_request(
            "/", "POST", query_string={"Key": "MessageGetLatest"}
        ).respond_with_data(f.read())

    return messaging_service.fetch_message_history()


def test_len(_message_history):
    assert len(_message_history) == 10


def test_first(_message_history):
    message = _message_history[0]
    assert message.id == "5bdf5147cc6ee1053d6ac1a4"


def test_last(_message_history):
    message = _message_history[-1]
    assert message.id == "5bdf51472322146c18b7348a"
