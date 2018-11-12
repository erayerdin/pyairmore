import ipaddress
import json
import unittest

import pyairmore.request
import pyairmore.request.messaging


class MessageHistoryRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.messaging.MessageHistoryRequest(
            cls.session
        )

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=MessageGetLatest"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")


class SendMessageRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.messaging.SendMessageRequest(
            cls.session, "321", "foo"
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )[0]  # type: dict
        else:
            cls.body = json.loads(cls.request.body)[0]  # type: dict

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=MessageSend"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_phone(self):
        self.assertEqual(self.body.get("Phone"), "321")

    def test_body_content(self):
        self.assertEqual(self.body.get("Content"), "foo")

    def test_body_uid(self):
        self.assertIsInstance(self.body.get("UniqueID"), str)
        self.assertGreater(len(self.body.get("UniqueID")), 0)


class ChatHistoryRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.request.messaging.ChatHistoryRequest(
            cls.session, "foo", 5, 15
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
        self.assertTrue(self.request.url.endswith("/?Key=MessageGetList"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_id(self):
        self.assertEqual(self.body.get("ID"), "foo")

    def test_body_start(self):
        self.assertEqual(self.body.get("Start"), 5)

    def test_body_limit(self):
        self.assertEqual(self.body.get("Limit"), 15)
