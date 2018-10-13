# todo [1] package doc
import typing

import requests

import pyairmore.request


class ServerIdleException(Exception):
    # todo 1 - class doc

    def __init__(self, service):
        message = "Server is found idle while making request for {}. The reasons might be:\n" \
                  " - You might not even have installed Airmore to your device.\n" \
                  " - Sometimes your Airmore server goes idle for battery. You need to open it up again.".format(
            service.__class__.__name__
        )
        super().__init__(message)


class AuthorizationException(Exception):
    # todo 1 - class doc

    def __init__(self):
        message = "You are not authorized for this session. Please accept authorization on your phone."
        super().__init__(message)


class Service:
    # todo 1 - class doc

    def __init__(self, session: pyairmore.request.AirmoreSession):
        # todo 2 - init doc

        self.session = session
        self._response = None  # type: requests.Response

    def request(self, process_type: typing.ClassVar["Process"]):
        is_running = self.session.is_server_running

        if not is_running:
            raise ServerIdleException(self)

        is_authorized = self.session.request_authorization()

        if not is_authorized:
            raise AuthorizationException()

        process = process_type(self)
        process.url = self.session.base_url + process.url
        self._response = self.session.send(process)


class Process(requests.PreparedRequest):
    # todo 1 - class doc

    def __init__(self, service: Service):
        # todo 2 - init doc
        super().__init__()

        self.service = service

    def prepare_url(self, url, params):
        super().prepare_url(url, params)
        self.url = self.service.session.base_url + url
