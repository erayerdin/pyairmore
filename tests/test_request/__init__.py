import pyairmore.request


class AirmoreRequestTestCase:
    request_class = None
    request_class_args = tuple()
    request_class_kwargs = dict()

    @classmethod
    def setup_class(cls):
        from ipaddress import IPv4Address

        session = pyairmore.request.AirmoreSession(IPv4Address("127.0.0.1"))
        cls.request = cls.request_class(
            session, *cls.request_class_args, **cls.request_class_kwargs
        )

    def test_url(self):
        raise NotImplementedError()
