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


class MessageComparisonTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.m1 = pyairmore.services.messaging.Message()
        cls.m2 = pyairmore.services.messaging.Message()
        cls.m3 = pyairmore.services.messaging.Message()

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
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )[0]  # type: dict
        else:
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


class ChatHistoryRequestTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.request = pyairmore.services.messaging.ChatHistoryRequest(
            cls.session, "foo", 5, 15
        )
        if isinstance(cls.request.body, bytes):
            cls.body = json.loads(
                cls.request.body.decode("utf-8")
            )  # type: dict
        else:
            cls.body = json.loads(cls.request.body)  # type: dict

    def test_url_startswith(self):
        self.assertTrue(self.request.url.startswith(self.session.base_url))

    def test_url_endswith(self):
        self.assertTrue(self.request.url.endswith("/?Key=MessageGetList"))

    def test_method(self):
        self.assertEqual(self.request.method, "POST")

    def test_body_id(self):
        self.assertEqual(self.body.get("ID"), "foo")

    def test_body_start(self):
        self.assertEqual(self.body.get("Start"), 5)

    def test_body_limit(self):
        self.assertEqual(self.body.get("Limit"), 15)


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


class MessagingServiceFetchChatHistoryTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.session = pyairmore.request.AirmoreSession(
            ipaddress.IPv4Address("127.0.0.1")
        )
        cls.service = pyairmore.services.messaging.MessagingService(
            cls.session
        )
        cls.message_id = "5bdf514735c35b82881109f7"
        cls.max_limit = 20

    def test_nonexistent_id(self):
        id = "foo"
        messages = self.service.fetch_chat_history(id)
        self.assertEqual(messages, [])

    def test_message_nostart_nolimit_first_id(self):
        messages = self.service.fetch_chat_history(self.message_id)
        message = messages[0]  # type: pyairmore.services.messaging.Message
        self.assertEqual(message.id, self.message_id)

    def test_message_nostart_nolimit_len(self):
        messages = self.service.fetch_chat_history(self.message_id)
        self.assertEqual(len(messages), 10)

    def test_message_nostart_50limit_first_id(self):
        messages = self.service.fetch_chat_history(self.message_id, limit=50)
        message = messages[0]
        self.assertEqual(message.id, self.message_id)

    def test_message_nostart_50limit_len(self):
        messages = self.service.fetch_chat_history(self.message_id, limit=50)
        self.assertEqual(len(messages), self.max_limit)

    def test_message_5start_nolimit_first_id(self):
        will_repeat = True

        while will_repeat:
            try:
                messages = self.service.fetch_chat_history(self.message_id,
                                                           start=5)
                message = messages[0]
                self.assertNotEqual(message.id, self.message_id)
                will_repeat = False
            except self.failureException:
                pass

    def test_message_5start_nolimit_len(self):
        messages = self.service.fetch_chat_history(self.message_id, start=5)
        self.assertEqual(len(messages), 10)

    def test_message_5start_50limit_len(self):
        messages = self.service.fetch_chat_history(self.message_id,
                                                   start=5,
                                                   limit=50)
        self.assertEqual(len(messages), 15)

    def test_fetch_via_message_object(self):
        messages = self.service.fetch_message_history()
        that_message_filter = filter(lambda m: m.id == self.message_id,
                                     messages)
        that_message = next(that_message_filter)

        chat = self.service.fetch_chat_history(that_message)
        self.assertNotEqual(chat, [])
