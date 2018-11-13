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
