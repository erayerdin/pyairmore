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

            s.type = d.get("AccountType", None)
            s.name = d.get("AccountName", None)
            _sources.add(s)

            g.id = str(d.get("ID", None))
            g.name = d.get("GroupName")
            g.source = s
            _groups.add(g)

        return _groups

    def create_group(self, name: str) -> pyairmore.data.contacts.Group:
        # todo 2 - method doc

        request = pyairmore.request.contacts.CreateGroupRequest(
            self.session, str(name)
        )
        response = self.session.send(request)
        group_id = str(response.json()[0]["ID"])
        self.get_groups()

        group = next(filter(lambda g: g.id == group_id, _groups))
        return group

    def update_group(self,  # todo 1 - bug - fix this
                     id_or_group: typing.Union[
                         int, pyairmore.data.contacts.Group
                     ],
                     name: str) -> pyairmore.data.contacts.Group:
        # todo 2 - method doc

        if isinstance(id_or_group, pyairmore.data.contacts.Group):
            group_id = int(id_or_group.id)
        else:
            group_id = int(id_or_group)

        request = pyairmore.request.contacts.UpdateGroupRequest(
            self.session, group_id, str(name)
        )
        self.session.send(request)
        self.get_groups()

        group = next(filter(lambda g: g.id == str(group_id), _groups))
        return group
