# todo 1 - doc for package
import ipaddress

import requests


class AirmoreSession(requests.Session):
    # todo 1 - doc for class

    def __init__(self, ip_address: ipaddress.IPv4Address, port: int = 2333):
        # todo 2 - doc for init
        super().__init__()

        self.ip_address = ip_address  # type: ipaddress.IPv4Address
        self.port = port  # type: int
        self.is_mocked = False

    @property
    def is_server_running(self) -> bool:
        response = self.post("/?Key=PhoneCheckAuthorization")
        body = response.text  # type: str

        is_running = False

        if body == '"0"':  # i don't know, server returns that if it is running
            is_running = True

        return is_running

    def request_authorization(self) -> bool:
        response = self.post("/?Key=PhoneRequestAuthorization")

        is_accepted = False

        if response.text == "true":
            is_accepted = True

        return is_accepted

    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None,
                timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None,
                json=None):
        # todo 1 - doc for method
        new_url = self.base_url + url

        return super().request(method, new_url, params, data, headers, cookies, files, auth, timeout, allow_redirects,
                               proxies, hooks, stream, verify, cert, json)

    @property
    def base_url(self) -> str:
        prefix = "http"

        if self.is_mocked:
            prefix = "mock"

        return "{}://{}:{}".format(prefix, self.ip_address, self.port)
