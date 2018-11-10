import unittest

import pyairmore.data.contacts


class SourceComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.s1 = pyairmore.data.contacts.Source()
        cls.s1.type = "com.foo"
        cls.s1.name = "foo@bar.baz"

        cls.s2 = pyairmore.data.contacts.Source()
        cls.s2.type = "com.foo"
        cls.s2.name = "foo@bar.baz"

        cls.s3 = pyairmore.data.contacts.Source()
        cls.s3.type = "com.bar"
        cls.s3.name = "foo@bar.baz"

    def test_equal(self):
        self.assertEqual(self.s1, self.s2)

    def test_not_equal(self):
        self.assertNotEqual(self.s1, self.s3)
        self.assertNotEqual(self.s2, self.s3)
