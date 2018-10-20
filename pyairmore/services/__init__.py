"""This package contains services to help developers access Airmore server.

Services represent different aspects of Airmore server.
"""
import typing

import requests

import pyairmore.request


class ServerUnreachableException(Exception):
    """
    This exception is thrown when:
     - No Airmore server was found on target session.
     - Airmore server is idle on target session.
    """

    def __init__(self, service):
        message = "Server is found idle while making request for {}. The reasons might be:\n" \
                  " - You might not even have installed Airmore to your device.\n" \
                  " - Sometimes your Airmore server goes idle for battery saving. You need to open it up again." \
            .format(service.__class__.__name__)
        super().__init__(message)


class AuthorizationException(Exception):
    """
    This exception is thrown when the authorization is rejected by the device.
    """

    def __init__(self):
        message = "You are not authorized for this session. Please accept authorization on target device."
        super().__init__(message)


class Service:
    """Service represents an aspect of Airmore, like messages, contacts and gallery, each is an aspect and has their
    services.

    This class is used to extend these aspects. You are likely to use this class if you plan to develop/extend the
    library. If you utilize the library, then you need to use other implementations, which are in their own modules.

    **Instance Attributes**
     - **session: pyairmore.request.AirmoreSession** -- Parent session.
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        """
        :param session: Session to wrap.
        """

        self.session = session
        # self._response = None  # type: requests.Response

    def request(self, process_type: typing.Type["Process"], **kwargs) -> requests.Response:
        """Request resource from Airmore server using a :class:`Process<pyairmore.services.Process>` instance.

        :param process_type: Process class to initialize.
        :param kwargs: Options to pass to the request. You can use any parameter that is used in requests to make
        requests.
        :return: Response object.
        """

        is_running = self.session.is_server_running

        if not is_running:
            raise ServerUnreachableException(self)

        is_authorized = self.session.is_authorized

        if not is_authorized:
            auth_request = self.session.request_authorization()

            if not auth_request:
                raise AuthorizationException()

        process = process_type(self)
        process.url = self.session.base_url + process.url
        return self.session.send(process, **kwargs)


class Process(requests.PreparedRequest):
    """Process represents a functionality of an aspect of Airmore, which is :class:`Service<pyairmore.services.Service>`.

    This class is used to extend these functionalities. You are likely to use this class if you plan to
    develop/extend the library. If you utilize the library, then you need to use other implementations, which are in
    their own modules.

    **Instance Attributes**
     - **service: pyairmore.services.Service** -- Parent service.
    """

    def __init__(self, service: Service):
        """
        :param service: Parent service.
        """
        super().__init__()

        self.service = service

    def prepare_url(self, url, params):
        super().prepare_url(url, params)
        self.url = self.service.session.base_url + url
