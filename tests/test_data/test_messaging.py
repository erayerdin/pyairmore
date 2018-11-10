import datetime
import unittest

import pyairmore.data.messaging
import pyairmore.request
import pyairmore.services.messaging


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
            "content": "Lorem ipsum"
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
