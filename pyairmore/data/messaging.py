"""Contains classes/methods for messaging aspect."""
import enum


class MessageType(enum.Enum):
    """Defines if the message was sent or received.

    | **RECEIVED (1)**: Target device received the message.
    | **SENT (2)**: Target device sent the message.
    """

    RECEIVED = 1
    SENT = 2


class Message:
    """A class that consists of information about a particular SMS."""

    def __init__(self):
        self.id = None  # type: str
        self.name = None  # type: str
        self.phone = None  # type: str
        self.datetime = None  # type_: datetime.datetime
        self.content = None  # type: str
        self.type = MessageType.RECEIVED  # type: MessageType
        self.was_read = True  # type: bool
        self.count = 1  # type: int

    def __eq__(self, other: "Message") -> bool:
        if self is other:  # pragma: no cover
            return True

        return all(
            (
                self.id == other.id,
                self.name == other.name,
                self.phone == other.phone,
                self.datetime == other.datetime,
                self.content == other.content,
                self.type == other.type,
            )
        )

    def __ne__(self, other: "Message") -> bool:
        return not self.__eq__(other)

    def __gt__(self, other: "Message") -> bool:
        return self.datetime > other.datetime

    def __ge__(self, other: "Message") -> bool:
        return self.datetime >= other.datetime

    def __lt__(self, other: "Message") -> bool:
        return self.datetime < other.datetime

    def __le__(self, other: "Message") -> bool:
        return self.datetime <= other.datetime
