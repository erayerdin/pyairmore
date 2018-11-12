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
