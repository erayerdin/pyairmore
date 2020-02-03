from ipaddress import IPv4Address

import pytest

from pyairmore.request import AirmoreSession


@pytest.fixture
def airmore_session(httpserver):
    return AirmoreSession(IPv4Address("127.0.0.1"), 2333)  # TODO will change to mock


@pytest.fixture
def airmore_request_factory(airmore_session):
    def factory(klass, *args, **kwargs):
        return klass(airmore_session, *args, **kwargs)

    return factory
