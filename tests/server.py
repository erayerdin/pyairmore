#!/usr/bin/env python3

from flask import Flask, jsonify, request, Response

app = Flask(__name__)


@app.route('/')
def path():
    arg = request.args.get("Key", None, str)

    with open("resources/test/home.txt", "r") as f:
        default_response = f.read()

    responses = (
        ("ResponseCheckAuthorization", lambda: Response('"0"', mimetype="text/plain")),
        ("PhoneRequestAuthorization", lambda: Response("true", mimetype="text/plain"))
    )

    for response in responses:
        if arg == response[0]:
            return response[1]()

    return Response(default_response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(port=2333)
