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
    def is_server_running(self) -> bool:
        """Whether the Airmore server runs or not.

        The server is connected via a socket connection.

        :return: True if the server runs.
        """

        if self.is_mocked:
            return True

        import socket
        from contextlib import closing

        is_running = False
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((str(self.ip_address), self.port)) == 0:
                is_running = True

        return is_running

    @property
    def is_application_open(self) -> bool:
        """Whether the application is open and front.

        This means the user now can see Airmore application on screen.

        :return: True if the application is open and front.
        """
        # now i know what you are thinking
        # i don't know what these devs were thinking
        # but, apparently, the url below checks if the application
        # is open and user can see it

        response = self.post("/?Key=PhoneCheckAuthorization")
        status = response.status_code
        body = response.text

        if status != 200:
            return False

        is_app_front = False

        if body == '"0"':
            is_app_front = True

        return is_app_front

    def request_authorization(self) -> bool:
        """Requests authorization from the device.

        This method will block the thread until the authorization accepted on the device. You might
        want to utilize async if you do not want to hang your application.

        The authorization on device will be rejected automatically after 30 seconds.

        Running this method before each request is a good practice since the target device will not show authorization
        dialog if the session is already authorized.

        :return: True if the authorization was accepted.
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
