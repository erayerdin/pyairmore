from pytest_httpserver import HTTPServer


def test_is_server_running(httpserver, airmore_session):
    assert airmore_session.is_server_running


def test_is_application_open_zero(
    httpserver: HTTPServer, authorization_required, airmore_session
):
    httpserver.expect_request(
        "/", "POST", query_string={"Key": "PhoneCheckAuthorization"}
    ).respond_with_data('"0"')
    assert airmore_session.is_application_open
