import ipaddress
import unittest
import urllib3.util.url

import pyairmore.request


class AirmoreRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )

    def setUp(self):
        super().setUp()
        self.request = pyairmore.request.AirmoreRequest(self.session)

    def test_method(self):
        self.request.prepare_method("get")
        self.assertEqual(self.request.method, "POST")

        self.request.prepare_method("whatever")
        self.assertEqual(self.request.method, "POST")

        self.request.prepare_method("post")
        self.assertEqual(self.request.method, "POST")

    def test_prepare_url_contains_base_url(self):
        self.request.prepare_url("/foo", {})
        self.assertEqual(
            self.session.base_url,
            self.request.url[: len(self.session.base_url)],
        )

    def test_prepare_url_without_params(self):
        self.request.prepare_url("/foo", {})
        self.assertEqual(self.request.url, self.session.base_url + "/foo")

    def test_prepare_url_with_params(self):
        self.request.prepare_url("/", {"foo": "bar"})
        self.assertEqual(self.request.url, self.session.base_url + "/?foo=bar")


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

    def test_base_url_scheme(self):
        parsed = urllib3.util.url.parse_url(self.session.base_url)
        self.assertEqual(parsed.scheme, "http")

    def test_base_url_hostname(self):
        parsed = urllib3.util.url.parse_url(self.session.base_url)
        self.assertEqual(parsed.hostname, "127.0.0.1")

    def test_base_url_port(self):
        parsed = urllib3.util.url.parse_url(self.session.base_url)
        self.assertEqual(parsed.port, 2333)
