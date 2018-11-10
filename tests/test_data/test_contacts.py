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


class GroupComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.g1 = pyairmore.data.contacts.Group()
        cls.g1.id = "1"
        cls.g1.name = "Foo"

        cls.g2 = pyairmore.data.contacts.Group()
        cls.g2.id = "1"
        cls.g2.name = "Foo"

        cls.g3 = pyairmore.data.contacts.Group()
        cls.g3.id = "1"
        cls.g3.name = "Bar"

        cls.g4 = pyairmore.data.contacts.Group()
        cls.g4.id = "2"
        cls.g4.name = "Foo"

    def test_equal(self):
        self.assertEqual(self.g1, self.g2)
        self.assertEqual(self.g1, self.g3)

    def test_not_equal(self):
        self.assertNotEqual(self.g1, self.g4)
        self.assertNotEqual(self.g2, self.g4)
        self.assertNotEqual(self.g3, self.g4)

    def test_equal_name_reassingment(self):
        self.assertEqual(self.g2, self.g3)
        self.assertEqual(self.g2.name, "Bar")
