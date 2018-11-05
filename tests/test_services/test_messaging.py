import datetime
import ipaddress
import json
import unittest

import pyairmore.services.messaging


class MessageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.messaging.MessagingService(
            cls.session
        )
        cls.messages = cls.service.fetch_message_history()

    def test_id_type(self):
        for m in self.messages:
            self.assertIsInstance(m.id, str)

    def test_name_type(self):
        for m in self.messages:
            self.assertIsInstance(m.name, str)

    def test_phone_type(self):
        for m in self.messages:
            self.assertIsInstance(m.phone, str)

    def test_datetime_type(self):
        for m in self.messages:
            self.assertIsInstance(m.datetime, datetime.datetime)

    def test_content(self):
        for m in self.messages:
            self.assertIsInstance(m.content, str)

    def test_type_type(self):
        for m in self.messages:
            self.assertIsInstance(
                m.type,
                pyairmore.services.messaging.MessageType
            )

    def test_was_read_type(self):
        for m in self.messages:
            self.assertIsInstance(m.was_read, bool)

    def test_count_type(self):
        for m in self.messages:
            self.assertIsInstance(m.count, int)

    def test_count_greater_than_zero(self):
        for m in self.messages:
            self.assertGreater(m.count, 0)


class MessageHistoryRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.services.messaging.MessageHistoryRequest(
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
        cls.request = pyairmore.services.messaging.SendMessageRequest(
            cls.session, "321", "foo"
        )
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


class MessagingServiceFetchMessageHistoryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.messaging.MessagingService(
            cls.session
        )
        cls.messages = cls.service.fetch_message_history()

    def test_return_type(self):
        self.assertTrue(hasattr(self.messages, "__iter__"))

    def test_children_type(self):
        for m in self.messages:
            self.assertIsInstance(m, pyairmore.services.messaging.Message)


class MessagingServiceSendMessageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.messaging.MessagingService(
            cls.session
        )

    def test_send_message_success(self):
        self.service.send_message("321", "lorem")

    def test_send_message_fail(self):
        with self.assertRaises(
                pyairmore.services.messaging.MessageRequestGSMError
        ):
            self.service.send_message("123", "ipsum")
