import ipaddress
import unittest

import pyairmore.request


class AirmoreSessionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )

    def test_is_server_running(self):
        self.assertTrue(self.session.is_server_running)

    def test_is_application_open(self):
        self.assertTrue(self.session.is_application_open)

    def test_request_authorization(self):
        self.assertTrue(self.session.request_authorization())

    def test_base_url(self):
        base_url = self.session.base_url
        self.assertEqual(base_url, "http://127.0.0.1:2333")
