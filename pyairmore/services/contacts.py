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

    @staticmethod
    def __get_group_id(id_or_group: typing.Union[
                           int, pyairmore.data.contacts.Group
                       ]) -> int:
        # todo 3 - doc - method

        if isinstance(id_or_group, pyairmore.data.contacts.Group):
            group_id = int(id_or_group.id)
        else:
            group_id = int(id_or_group)

        return group_id

    def update_group(self,
                     id_or_group: typing.Union[
                         int, pyairmore.data.contacts.Group
                     ],
                     name: str) -> pyairmore.data.contacts.Group:
        # todo 2 - method doc

        group_id = self.__get_group_id(id_or_group)
        request = pyairmore.request.contacts.UpdateGroupRequest(
            self.session, group_id, str(name)
        )
        self.session.send(request)
        self.get_groups()

        group = next(filter(lambda g: g.id == str(group_id), _groups))
        return group

    def delete_group(self,
                     id_or_group: typing.Union[
                         int, pyairmore.data.contacts.Group
                     ]) -> bool:
        # todo 2 - doc - method

        group_id = self.__get_group_id(id_or_group)
        request = pyairmore.request.contacts.DeleteGroupRequest(
            self.session, group_id
        )
        self.session.send(request)
        groups = self.get_groups()

        group = next(filter(lambda g: g.id == str(group_id), groups), None)

        if group:
            return False

        return True
