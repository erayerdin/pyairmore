# todo 1 - module doc
import typing

import datetime
import enum

import pyairmore


class MessageType(enum.Enum):
    # todo 1 - class doc

    RECEIVED = 1
    SENT = 2


class Message:
    # todo 1 - class doc

    def __init__(self):
        self.id = None  # type: str
        self.name = None  # type: str
        self.phone = None  # type: str
        self.datetime = None  # type: datetime.datetime
        self.content = None  # type: str
        self.type = MessageType.RECEIVED  # type: MessageType
        self.was_read = True  # type: bool
        self.count = 1  # type: int


class MessageHistoryRequest(pyairmore.request.AirmoreRequest):
    """A request to get latest messages.

    | **Endpoint:** /?Key=MessageGetLatest
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

        self.prepare_url("/", {"Key": "MessageGetLatest"})


class MessagingService(pyairmore.services.Service):
    # todo 1 - class doc

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

    def fetch_message_history(self) -> typing.List[Message]:
        # todo 2 - method doc

        request = MessageHistoryRequest(self.session)
        response = self.session.send(request)

        messages = []
        data = response.json()  # type: typing.List[dict]

        for d in data:
            message = Message()

            message.id = d.get("ID", None)
            message.name = d.get("ShowName", None)
            message.phone = d.get("Phone", None)

            # parsing datetime
            date_str = d.get("Date", None)  # type: str
            if date_str is not None:
                date_str = str(date_str)
                date_format = "%Y/%m/%d %H:%M:%S"

                message.datetime = datetime.datetime.strptime(
                    date_str,
                    date_format
                )

            message.content = d.get("Content", None)

            # detecting type
            message_type = d.get("MsgType", None)
            if message_type and message_type != 1:
                message.type = MessageType.SENT

            # was read
            read = d.get("Read", 1)
            if read != 1:
                message.was_read = False

            message.count = d.get("Count", 1)
            messages.append(message)

        return messages


__all__ = [
    "MessagingService"
]
