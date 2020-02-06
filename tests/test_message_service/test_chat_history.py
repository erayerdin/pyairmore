import pytest
from pytest_httpserver import HTTPServer


@pytest.fixture
def _chat_history_mock_factory(httpserver: HTTPServer):
    def factory(limit):
        if limit == 5:
            with open("resources/test/message_get_list_0_5.json", "rb") as f:
                httpserver.expect_request(
                    "/", "POST", query_string={"Key": "MessageGetList"}
                ).respond_with_data(f.read())
        else:
            with open("resources/test/message_get_list_0_10.json", "rb") as f:
                httpserver.expect_request(
                    "/", "POST", query_string={"Key": "MessageGetList"}
                ).respond_with_data(f.read())

    return factory


def test_limit_5_len(_chat_history_mock_factory, messaging_service):
    _chat_history_mock_factory(5)
    messages = messaging_service.fetch_chat_history("5bdd46f06905c8a085247638", 0, 5)
    assert len(messages) == 5


def test_limit_10_len(_chat_history_mock_factory, messaging_service, message):
    _chat_history_mock_factory(10)
    messages = messaging_service.fetch_chat_history(message, 0, 10)
    assert len(messages) == 10
