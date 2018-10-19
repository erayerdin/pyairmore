"""
``request`` module contains some classes extending another classes from ``requests`` package to make easier requests
to an Airmore server.
"""
import ipaddress

import requests
import requests.exceptions


class AirmoreSession(requests.Session):
    """``AirmoreSession`` extends ``requests.Session`` in order to manage an Airmore session.

    **Instance Attributes**
     - **ip_address: ipaddress.IPv4Address** -- IP address to connect to.
     - **port: int** -- Port to connect to.
     - **is_mocked: bool** -- Whether the connection is mocked. It is utilized in unit-tests.

    **Notes**

    An ``AirmoreSession`` instance will manage URLs differently. It uses its ``ip_address`` and ``port`` to prefix a
    custom URL on each request. Such as::

     >>> from ipaddress import IPv4Address
     >>> session = AirmoreSession(IPv4Address("127.0.0.1"))
     >>> session.get("/whatever")

    will use the url below to make request::

     >>> "http://127.0.0.1:2333/whatever"
    """

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int = 2333):
        """
        :param ip_address: IP address to connect to.
        :param port: Port to connect to.
        """
        super().__init__()

        self.ip_address = ip_address  # type: ipaddress.IPv4Address
        self.port = port  # type: int
        self.is_mocked = False

    @property
    def is_server_running(self) -> bool:  # todo 1 - review and refactor is_server_running
        """Whether the Airmore server runs or not.

        This property method checks and fails under the conditions below:
         - The server has not been responding for 2 seconds.
         - The server returns '"1"'. Airmore server returns this string when it is running but server not activated and
           will not be able to accept authorization requests.

        :return: True if it runs.
        """

        try:
            response = self.post("/?Key=PhoneCheckAuthorization", timeout=2)
        except requests.exceptions.ConnectionError:
            return False

        body = response.text  # type: str

        is_running = False

        if body == '"0"':  # i don't know, server returns that if it is running
            is_running = True

        return is_running

    @property
    def is_authorized(self) -> bool:  # todo 1 - implement is_authorized
        raise NotImplementedError

    def request_authorization(self) -> bool:  # todo 1 - review and refactor request_authorization
        """Requests authorization from the device.

        This method will block the thread for 30 seconds until the authorization accepted on the device. You might
        want to utilize async if you do not want to hang your application.

        The authorization on device will be rejected automatically after 30 seconds.

        It is better to use ``is_server_running`` property to ensure your server is running before using this
        method.

        :return: True if the authorization accepted.
        """

        response = self.post("/?Key=PhoneRequestAuthorization")

        is_accepted = False

        if response.text == "true":
            is_accepted = True

        return is_accepted

    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None,
                timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None,
                json=None) -> requests.Response:
        new_url = self.base_url + url

        return super().request(method, new_url, params, data, headers, cookies, files, auth, timeout, allow_redirects,
                               proxies, hooks, stream, verify, cert, json)

    @property
    def base_url(self) -> str:
        """Constructs a base url (prefix) for any request.

        If ``is_mocked`` attribute is ``True``, then it will construct on ``mock`` protocol instead of ``http``.

        :return: A base url for internal requests.
        """

        prefix = "http"

        if self.is_mocked:
            prefix = "mock"

        return "{}://{}:{}".format(prefix, self.ip_address, self.port)


__all__ = [
    "AirmoreSession",
]
