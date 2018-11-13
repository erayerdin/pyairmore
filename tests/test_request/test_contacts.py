import ipaddress
import json
import unittest

import pyairmore.request
import pyairmore.request.contacts


class GroupsRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.contacts.GroupsRequest(
            cls.session
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )  # type: dict
        else:
            cls.body = json.loads(cls.request.body)  # type: dict

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=ContactGroupGetList"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_empty(self):
        self.assertEqual(self.body, dict())


class CreateGroupRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.contacts.CreateGroupRequest(
            cls.session,
            "foo"
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )  # type: list
        else:
            cls.body = json.loads(cls.request.body)  # type: list

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=ContactAddGroup"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_parent_type(self):
        self.assertIsInstance(self.body, list)

    def test_body_children_type(self):
        for d in self.body:  # type: dict
            self.assertIsInstance(d, dict)

    def test_body_children_has_key_name(self):
        for d in self.body:  # type: dict
            self.assertIn("GroupName", d)


class UpdateGroupRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.contacts.UpdateGroupRequest(
            cls.session, 1, "foo"
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )  # type: list
        else:
            cls.body = json.loads(cls.request.body)  # type: list

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=ContactUpdateGroup"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_parent_type(self):
        self.assertIsInstance(self.body, list)

    def test_body_children_type(self):
        for d in self.body:  # type: dict
            self.assertIsInstance(d, dict)

    def test_body_children_has_key_name(self):
        for d in self.body:  # type: dict
            self.assertIn("GroupName", d)

    def test_body_children_has_key_id(self):
        for d in self.body:  # type: dict
            self.assertIn("ID", d)
