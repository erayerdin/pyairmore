# todo 1 - module doc
import uuid

import pyairmore.request


class MessageHistoryRequest(pyairmore.request.AirmoreRequest):
    """A request to get latest messages.

    | **Endpoint:** /?Key=MessageGetLatest
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

        self.prepare_url("/", {"Key": "MessageGetLatest"})


class SendMessageRequest(pyairmore.request.AirmoreRequest):
    """A request to send message.

    | **Endpoint:** /?Key=MessageSend
    """

    def __init__(self,
                 session: pyairmore.request.AirmoreSession,
                 phone: str,
                 content: str):
        """
        :param session: Session object, which will be passed to super init.
        :param phone: Phone to send message to.
        :param content: Message content.
        """

        super().__init__(session)

        self.prepare_url("/", {"Key": "MessageSend"})
        self.prepare_headers({})

        data = {
            "Phone": str(phone),
            "Content": str(content),
            "UniqueID": uuid.uuid1().hex
        }
        self.prepare_body("", None, [data])


class ChatHistoryRequest(pyairmore.request.AirmoreRequest):
    """A request to see a particular chat's history.

    | **Endpoint:** /?Key=MessageGetList
    """

    def __init__(self,
                 session: pyairmore.request.AirmoreSession,
                 id: str,
                 start: int = 0,
                 limit: int = 10):
        """
        :param session: Session object, which will be passed to super init.
        :param id: ID of message.
        :param start: Start point.
        :param limit: Limit of messages.
        """

        super().__init__(session)

        self.prepare_url("/", {"Key": "MessageGetList"})
        self.prepare_headers({})

        data = {
            "ID": str(id),
            "Start": int(start),
            "Limit": int(limit)
        }
        self.prepare_body("", None, data)
