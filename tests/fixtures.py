import pytest

import pyairmore.request


@pytest.fixture
def airmore_session():
    from ipaddress import IPv4Address

    return pyairmore.request.AirmoreSession(IPv4Address("127.0.0.1"))
