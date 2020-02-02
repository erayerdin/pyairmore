import datetime
import ipaddress
import unittest

import pyairmore.data
import pyairmore.request
import pyairmore.services


class MessageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.messaging.MessagingService(cls.session)
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
            self.assertIsInstance(m.type, pyairmore.data.messaging.MessageType)

    def test_was_read_type(self):
        for m in self.messages:
            self.assertIsInstance(m.was_read, bool)

    def test_count_type(self):
        for m in self.messages:
            self.assertIsInstance(m.count, int)

    def test_count_greater_than_zero(self):
        for m in self.messages:
            self.assertGreater(m.count, 0)


class MessageComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.m1 = pyairmore.data.messaging.Message()
        cls.m2 = pyairmore.data.messaging.Message()
        cls.m3 = pyairmore.data.messaging.Message()

        now = datetime.datetime.now()
        eq_attrs = {
            "id": "1",
            "name": "Foo",
            "phone": "123",
            "datetime": now,
            "content": "Lorem ipsum",
        }

        for k, v in eq_attrs.items():
            setattr(cls.m1, k, v)
            setattr(cls.m2, k, v)
            setattr(cls.m3, k, v)

        cls.m3.name = "Bar"
        cls.m3.datetime = now + datetime.timedelta(days=1)

    def test_equal(self):
        self.assertEqual(self.m1, self.m2)

    def test_not_equal(self):
        self.assertNotEqual(self.m1, self.m3)
        self.assertNotEqual(self.m2, self.m3)

    def test_greater(self):
        self.assertGreater(self.m3, self.m1)
        self.assertGreater(self.m3, self.m2)

    def test_greater_equal(self):
        self.assertGreaterEqual(self.m3, self.m1)
        self.assertGreaterEqual(self.m3, self.m2)
        self.assertGreaterEqual(self.m1, self.m2)
        self.assertGreaterEqual(self.m2, self.m1)

    def test_less(self):
        self.assertLess(self.m1, self.m3)
        self.assertLess(self.m2, self.m3)

    def test_less_equal(self):
        self.assertLessEqual(self.m1, self.m3)
        self.assertLessEqual(self.m2, self.m3)
        self.assertLessEqual(self.m2, self.m1)
        self.assertLessEqual(self.m1, self.m2)
