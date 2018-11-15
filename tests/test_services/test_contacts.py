import unittest
import ipaddress

import pyairmore.request
import pyairmore.services.contacts
import pyairmore.data.contacts


class ContactsGroupsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )

    def test_group_service_get_groups_is_groups(self):
        service = pyairmore.services.contacts.GroupService(self.session)
        groups = service.get_groups()

        self.assertIs(groups, pyairmore.services.contacts._groups)


class GroupServiceGetGroupsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.contacts.GroupService(
            cls.session
        )
        cls.groups = cls.service.get_groups()

    def test_return_type(self):
        self.assertTrue(hasattr(self.groups, "__iter__"))

    def test_children_type(self):
        for g in self.groups:
            self.assertIsInstance(g, pyairmore.data.contacts.Group)


class GroupServiceCreateGroupTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.contacts.GroupService(
            cls.session
        )

    def test_group_name(self):
        group = self.service.create_group("foo")
        self.assertEqual(group.name, "foo")

    def test_group_source_type(self):
        source = self.service.create_group("foo").source
        self.assertEqual(source.type, "pyairmore")

    def test_group_source_name(self):
        source = self.service.create_group("foo").source
        self.assertEqual(source.name, "baz")


class GroupServiceUpdateGroupTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.contacts.GroupService(
            cls.session
        )

    def test_update_name(self):
        groups = self.service.get_groups()
        former_group = next(filter(lambda g: g.id == "2", groups))
        former_group_name = former_group.name

        self.service.update_group(former_group.id, "foo")
        groups = self.service.get_groups()
        latter_group = next(filter(lambda g: g.id == "2", groups))
        latter_group_name = latter_group.name

        self.assertNotEqual(former_group_name, latter_group_name)


class GroupServiceDeleteGroupTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.contacts.GroupService(
            cls.session
        )

    @unittest.skip("bug to be fixed")
    def test_delete(self):  # todo 2 - bug - fix test
        groups = self.service.get_groups()
        group = next(filter(lambda g: g.id == "1", groups), None)
        self.assertIsNotNone(group)

        was_deleted = self.service.delete_group(1)
        self.assertTrue(was_deleted)
        groups = self.service.get_groups()
        group = next(filter(lambda g: g.id == "1", groups), None)
        self.assertIsNone(group)
