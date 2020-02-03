import pytest

import pyairmore.data.messaging
import pyairmore.request.messaging
import pyairmore.services.messaging
from pyairmore.services.messaging import MessagingService


@pytest.fixture
def _messaging_service(airmore_session):
    return MessagingService(airmore_session)


@pytest.fixture
def _messaging_service_fetch_message_history(_messaging_service):
    return _messaging_service.fetch_message_history()


class TestMessagingServiceFetchMessageHistory:
    # TODO refactor tests
    def test_return_type(self, _messaging_service_fetch_message_history):
        assert hasattr(_messaging_service_fetch_message_history, "__iter__")

    def test_children_type(self, _messaging_service_fetch_message_history):
        for m in _messaging_service_fetch_message_history:
            assert isinstance(m, pyairmore.data.messaging.Message)


class TestMessagingServiceSendMessage:
    def test_send_message_success(self, _messaging_service):
        _messaging_service.send_message("321", "lorem")  # won't raise error

    def test_send_message_fail(self, _messaging_service):
        with pytest.raises(pyairmore.services.messaging.MessageRequestGSMError):
            _messaging_service.send_message("123", "ipsum")


class TestMessagingServiceFetchChatHistory:
    @classmethod
    def setup_class(cls):
        cls.message_id = "5bdf514735c35b82881109f7"
        cls.max_limit = 20

    def test_nonexistent_id(self, _messaging_service):
        # noinspection PyShadowingBuiltins
        id = "foo"
        messages = _messaging_service.fetch_chat_history(id)
        assert messages == []

    def test_message_nostart_nolimit_first_id(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(self.message_id)
        # noinspection PyUnresolvedReferences
        message = messages[0]  # type: pyairmore.services.messaging.Message
        assert message.id == self.message_id

    def test_message_nostart_nolimit_len(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(self.message_id)
        assert len(messages) == 10

    def test_message_nostart_50limit_first_id(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(self.message_id, limit=50)
        message = messages[0]
        assert message.id == self.message_id

    def test_message_nostart_50limit_len(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(self.message_id, limit=50)
        assert len(messages) == self.max_limit

    def test_message_5start_nolimit_first_id(self, _messaging_service):
        will_repeat = True

        while will_repeat:
            try:
                messages = _messaging_service.fetch_chat_history(
                    self.message_id, start=5
                )
                message = messages[0]
                assert message.id != self.message_id
                will_repeat = False
            except self.failureException:
                pass

    def test_message_5start_nolimit_len(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(self.message_id, start=5)
        assert len(messages) == 10

    def test_message_5start_50limit_len(self, _messaging_service):
        messages = _messaging_service.fetch_chat_history(
            self.message_id, start=5, limit=50
        )
        assert len(messages) == 15

    def test_fetch_via_message_object(self, _messaging_service):
        messages = _messaging_service.fetch_message_history()
        that_message_filter = filter(lambda m: m.id == self.message_id, messages)
        that_message = next(that_message_filter)

        chat = _messaging_service.fetch_chat_history(that_message)
        assert chat != []
