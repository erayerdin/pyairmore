import ipaddress
import requests_mock
import unittest

import pyairmore.request


class MockedAirmoreSession(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.adapter = requests_mock.Adapter()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1"), 2333
        )

        cls._mount()
        cls._register()

    @classmethod
    def _mount(cls):
        cls.session.is_mocked = True
        cls.session.mount(
            'mock',
            cls.adapter
        )

    @classmethod
    def _register(cls):
        cls.__register_phone_check_authorization()
        cls.__register_phone_request_authorization()

    @classmethod
    def __register_phone_check_authorization(cls):
        cls.adapter.register_uri(
            "POST",
            "/?Key=PhoneCheckAuthorization",
            text='"0"'
        )

    @classmethod
    def __register_phone_request_authorization(cls):
        cls.adapter.register_uri(
            "POST",
            "/?Key=PhoneRequestAuthorization",
            text="true"
        )


class AirmoreSessionTestCase(MockedAirmoreSession):
    def test_is_server_running(self):
        self.assertTrue(self.session.is_server_running)

    def test_is_application_open(self):
        self.assertTrue(self.session.is_application_open)

    def test_request_authorization(self):
        self.assertTrue(self.session.request_authorization())

    def test_base_url(self):
        base_url = self.session.base_url
        self.assertEqual(base_url, "mock://127.0.0.1:2333")
