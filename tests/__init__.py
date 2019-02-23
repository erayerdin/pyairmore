import httpretty
import unittest


class HTTPrettyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        httpretty.enable()

    @classmethod
    def tearDownClass(cls):
        httpretty.disable()
