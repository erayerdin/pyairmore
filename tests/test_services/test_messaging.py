import ipaddress
import unittest
import datetime

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
