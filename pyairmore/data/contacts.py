"""Contains classes/methods for contacts aspect."""


class Source:
    # todo 1 - class doc

    def __init__(self):
        self.type = None  # type: str
        self.name = None  # type: str

    def __eq__(self, other: "Source") -> bool:
        if self is other:
            return True

        return all((
            self.type == other.type,
            self.name == other.name,
        ))

    def __ne__(self, other: "Source") -> bool:
        return not self.__eq__(other)


class Group:
    # todo 1 - class doc

    def __init__(self):
        self.id = None  # type: str
        self.name = None  # type: str

    def __eq__(self, other: "Group") -> bool:
        if self is other:
            return True

        val = all((
            self.id == other.id,
        ))

        # change name
        self.name = other.name

        return val

    def __ne__(self, other: "Group") -> bool:
        return not self.__eq__(other)
