"""Contains ``AirmoreRequest`` classes for contacts aspect."""
import pyairmore


class GroupsRequest(pyairmore.request.AirmoreRequest):
    """A request to get groups.

    | **Endpoint:** /?Key=ContactGroupGetList
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

        self.prepare_url("/", {"Key": "ContactGroupGetList"})
        self.prepare_headers({})
        self.prepare_body("", None, {})


class CreateGroupRequest(pyairmore.request.AirmoreRequest):
    """A request to create a group.

    | **Endpoint:** /?Key=ContactAddGroup
    """

    def __init__(self, session: pyairmore.request.AirmoreSession, name: str):
        super().__init__(session)

        self.prepare_url("/", {"Key": "ContactAddGroup"})
        self.prepare_headers({})
        self.prepare_body("", None, [{"GroupName": str(name)}])


class UpdateGroupRequest(pyairmore.request.AirmoreRequest):
    """A request to create a group.

    | **Endpoint:** /?Key=ContactUpdateGroup
    """

    # noinspection PyShadowingBuiltins
    def __init__(self,
                 session: pyairmore.request.AirmoreSession,
                 id: int,
                 name: str):
        super().__init__(session)

        self.prepare_url("/", {"Key": "ContactUpdateGroup"})
        self.prepare_headers({})
        self.prepare_body("", None, [{"ID": int(id), "GroupName": str(name)}])
