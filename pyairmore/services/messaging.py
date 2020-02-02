"""Service and utilities related to messaging aspect."""
import datetime
import typing

import requests

import pyairmore
import pyairmore.data.messaging
import pyairmore.request.messaging


class MessageRequestGSMError(Exception):
    """Raised when "/?Key=MessageSend" does not return "2" to imply that
    something bad happened on the server side.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        message = "Message could not be sent due to GSM connectivity."
        super().__init__(message, *args, **kwargs)


class MessagingService(pyairmore.services.Service):
    """A service to manage and send messages."""

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

    @staticmethod
    def __convert_list_json_to_messages(
        response: requests.Response,
    ) -> typing.List[pyairmore.data.messaging.Message]:
        """Will convert a message response from Airmore server to a list of
        ``Message`` objects.
        """

        messages = []
        data = response.json()  # type: typing.List[dict]

        for d in data:
            message = pyairmore.data.messaging.Message()

            message.id = d.get("ID", None)
            message.name = d.get("ShowName", None)
            message.phone = d.get("Phone", None)

            # parsing datetime
            date_str = d.get("Date", None)  # type: str
            if date_str is not None:
                date_str = str(date_str)
                date_format = "%Y/%m/%d %H:%M:%S"

                message.datetime = datetime.datetime.strptime(date_str, date_format)

            message.content = d.get("Content", None)

            # detecting type
            message_type = d.get("MsgType", None)
            if message_type and message_type != 1:
                message.type = pyairmore.data.messaging.MessageType.SENT

            # was read
            read = d.get("Read", 1)
            if read != 1:
                message.was_read = False

            message.count = d.get("Count", 1)
            messages.append(message)

        return messages

    def fetch_message_history(self) -> typing.List[pyairmore.data.messaging.Message]:
        """Gets latest messages from your phone. These messages will be
        historically descending order.

        Will return empty list if could not be found.
        """

        request = pyairmore.request.messaging.MessageHistoryRequest(self.session)
        response = self.session.send(request)

        return self.__convert_list_json_to_messages(response)

    def send_message(
        self,
        contact_or_phone: typing.Union[str],
        # todo 3 - support contact
        content: str,
    ) -> None:
        """Sends a single message.

        .. note::

            Contact services will be provided on a future release. Ignore the
            term "contact" in ``contact_or_phone`` parameter.

        :raises MessageRequestGSMError:
        """

        request = pyairmore.request.messaging.SendMessageRequest(
            self.session, contact_or_phone, content
        )
        response = self.session.send(request)

        if response.text != "2":
            raise MessageRequestGSMError()

    def fetch_chat_history(
        self,
        message_or_id: typing.Union[pyairmore.data.messaging.Message, str],
        start: int = 0,
        limit: int = 10,
    ) -> typing.List[pyairmore.data.messaging.Message]:
        """Fetches a chat that a particular message is in. These messages will
        be historically descending order.

        Will return empty list if could not be found.

        :param message_or_id: ``Message`` object or a ``str`` id.
        :param start: Starting point.
        :param limit: Limit of messages to fetch.
        """

        if isinstance(message_or_id, pyairmore.data.messaging.Message):
            message_id = message_or_id.id
        else:
            message_id = str(message_or_id)

        start = int(start)
        limit = int(limit)

        request = pyairmore.request.messaging.ChatHistoryRequest(
            self.session, message_id, start, limit
        )
        response = self.session.send(request)

        return self.__convert_list_json_to_messages(response)
