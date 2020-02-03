def test_is_server_running(httpserver, airmore_session):
    assert airmore_session.is_server_running
