import datetime

import pytest

import pyairmore.data.messaging
import pyairmore.request
import pyairmore.services


@pytest.fixture
def _message_factory():
    def factory(**kwargs):
        m = pyairmore.data.messaging.Message()
        m.id = kwargs.get("id", "1")
        m.name = kwargs.get("name", "Foo")
        m.phone = kwargs.get("phone", "123")
        m.content = kwargs.get("content", "Lorem ipsum")
        m.datetime = kwargs.get("datetime", datetime.datetime.now())
        return m

    return factory


class TestMessageComparison:
    def test_equal(self, _message_factory):
        m1 = _message_factory()
        m2 = m1
        assert m1 == m2

    def test_not_equal(self, _message_factory):
        m1 = _message_factory()
        m2 = _message_factory()
        m3 = _message_factory(
            datetime=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        assert m1 != m3
        assert m2 != m3

    def test_greater(self, _message_factory):
        m1 = _message_factory()
        m2 = _message_factory()
        m3 = _message_factory(
            datetime=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        assert m3 > m1
        assert m3 > m2

    def test_greater_equal(self, _message_factory):
        m1 = _message_factory()
        m2 = m1
        m3 = _message_factory(
            datetime=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        assert m3 >= m1
        assert m3 >= m2
        assert m1 >= m2
        assert m2 >= m1

    def test_less(self, _message_factory):
        m1 = _message_factory()
        m2 = _message_factory()
        m3 = _message_factory(
            datetime=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        assert m1 < m3
        assert m2 < m3

    def test_less_equal(self, _message_factory):
        m1 = _message_factory()
        m2 = m1
        m3 = _message_factory(
            datetime=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        assert m1 <= m3
        assert m2 <= m3
        assert m2 <= m1
        assert m1 <= m2
