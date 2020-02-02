"""``request`` package contains some classes extending another classes from
``requests`` package to make easier requests to an Airmore server. """

import ipaddress
import socket
from contextlib import closing

import requests.exceptions


class AirmoreRequest(requests.PreparedRequest):
    """A PreparedRequest for Airmore server."""

    def __init__(self, session: "AirmoreSession"):
        super().__init__()
        self.__session = session  # type: AirmoreSession
        self.prepare_method(None)

    def prepare_method(self, method):
        """Will generate "POST" no matter what."""
        self.method = "POST"

    def prepare_url(self, url, params):
        """URL will have ``self._session.base_url``. Only path should be
        provided. For example::

            prepare_url("/foo", {"bar":"baz"})

        will provide::

            self.url  # http://host:port/foo?bar=baz

        depending on your ``self.__session``.
        """
        super().prepare_url(self.__session.base_url + url, params)


class ApplicationOpenRequest(AirmoreRequest):
    """A request to check if application is open."""

    def __init__(self, session: "AirmoreSession"):
        super().__init__(session)
        self.prepare_url("/", {"Key": "PhoneCheckAuthorization"})


class AuthorizationRequest(AirmoreRequest):
    """A request to request application or check if the session is already
    authorized."""

    def __init__(self, session: "AirmoreSession"):
        super().__init__(session)
        self.prepare_url("/", {"Key": "PhoneRequestAuthorization"})


class AirmoreSession(requests.Session):
    """``AirmoreSession`` extends ``requests.Session`` in order to manage an
    Airmore session. """

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int = 2333):
        """
        :param ip_address: IP address to connect to.
        :param port: Port to connect to.
        """
        super().__init__()

        self.ip_address = ip_address  # type: ipaddress.IPv4Address
        self.port = port  # type: int

    @property
    def is_server_running(self) -> bool:
        """Whether the Airmore server runs or not.

        The server is connected via a socket connection.

        :return: True if the server runs.
        """
        is_running = False
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock_val = sock.connect_ex((str(self.ip_address), self.port))
            print(sock_val)
            if sock_val == 0:
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

        request = ApplicationOpenRequest(self)
        response = self.send(request)
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

        This method will block the thread until the authorization accepted
        on the device. You might want to utilize async if you do not want to
        hang your application.

        The authorization on device will be rejected automatically after 30
        seconds.

        Running this method before each request is a good practice since the
        target device will not show authorization dialog if the session is
        already authorized.

        :return: True if the authorization was accepted.
        """

        request = AuthorizationRequest(self)
        response = self.send(request, False)

        is_accepted = False

        if response.text == "true":
            is_accepted = True

        return is_accepted

    def send(
        self,
        request: AirmoreRequest,
        force_authorization: bool = True,
        force_connectivity_check: bool = True,
        **kwargs
    ) -> requests.Response:
        """Sending request with an ``AirmoreRequest``."""

        if force_connectivity_check:
            is_connectivity_present = self.is_server_running

            if not is_connectivity_present:
                raise ServerUnreachableException()

        if force_authorization:
            is_authorized = self.request_authorization()

            if not is_authorized:
                raise AuthorizationException()

        return super().send(request, **kwargs)

    @property
    def base_url(self) -> str:
        """Constructs a base url (prefix) for any AirmoreRequest.

        :return: A base url for internal requests.
        """

        return "http://{}:{}".format(self.ip_address, self.port)


class ServerUnreachableException(Exception):
    """
    This exception is thrown when:
     - No Airmore server was found on target session.
     - Airmore server is idle on target session.
    """

    def __init__(self):
        message = (
            "Server is found idle. The reasons might be:\n"
            "- You might not even have installed Airmore to your "
            "device.\n"
            "- Sometimes your Airmore server goes idle for battery "
            "saving. You need to open it up again. "
        )
        super().__init__(message)


class AuthorizationException(Exception):
    """
    This exception is thrown when the authorization is rejected by the device.
    """

    def __init__(self):
        message = (
            "Could not authorize. Please accept authorization on " "target device. "
        )
        super().__init__(message)
