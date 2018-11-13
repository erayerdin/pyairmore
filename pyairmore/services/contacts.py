"""Services related to contacts aspect."""
import typing

import pyairmore
import pyairmore.request
import pyairmore.request.contacts
import pyairmore.data.contacts

# noinspection PyUnresolvedReferences
_groups = set()  # type: typing.Set[pyairmore.data.contacts.Group]
# noinspection PyUnresolvedReferences
_sources = set()  # type: typing.Set[pyairmore.data.contacts.Source]


class GroupService(pyairmore.services.Service):
    # todo 1 - class doc

    def __init__(self, session: pyairmore.request.AirmoreSession):
        super().__init__(session)

    def get_groups(self) -> typing.Set[pyairmore.data.contacts.Group]:
        # todo 2 - method doc

        request = pyairmore.request.contacts.GroupsRequest(self.session)
        response = self.session.send(request)

        data = response.json()  # type: typing.List[dict]

        for d in data:
            g = pyairmore.data.contacts.Group()
            s = pyairmore.data.contacts.Source()

            g.id = str(d.get("ID", None))
            g.name = d.get("GroupName")
            _groups.add(g)

            s.type = d.get("AccountType", None)
            s.name = d.get("AccountName", None)
            _sources.add(s)

        return _groups
