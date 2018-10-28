#!/usr/bin/env python3

import typing
from flask import Flask, jsonify, request, Response

app = Flask(__name__)


def get_device_info() -> Response:
    with open("resources/test/device_detail.txt", "r") as f:
        return Response(f.read(), mimetype="text/plain")


def refresh_screen() -> Response:
    with open("resources/test/screenshot.txt", "r") as f:
        return Response(f.read(), mimetype="text/plain")


@app.route('/', methods=["GET", "POST"])
def path():
    arg = request.args.get("Key", None, str)

    with open("resources/test/home.txt", "r") as f:
        default_response = f.read()

    responses = (
        ("PhoneCheckAuthorization", lambda: Response('"0"', mimetype="text/plain")),
        ("PhoneRequestAuthorization", lambda: Response("true", mimetype="text/plain")),
        ("PhoneGetDeviceInfo", get_device_info),
        ("PhoneRefreshScreen", refresh_screen)
    )  # type: typing.Tuple[typing.Tuple[str, callable]]

    for response in responses:
        if arg == response[0]:
            return response[1]()

    return Response(default_response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(port=2333)
