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
