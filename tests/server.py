#!/usr/bin/env python3
import random

import json
import typing
# noinspection PyPackageRequirements
from flask import Flask, request, Response

app = Flask(__name__)


def get_device_info() -> Response:
    with open("resources/test/device_detail.txt", "r") as f:
        return Response(f.read(), mimetype="text/plain")


def refresh_screen() -> Response:
    with open("resources/test/screenshot.txt", "r") as f:
        return Response(f.read(), mimetype="text/plain")


def message_get_latest() -> Response:
    with open("resources/test/message_get_latest.txt", "r") as f:
        return Response(f.read(), mimetype="text/plain")


def message_send() -> Response:
    data = request.get_json(silent=True)  # type: list

    if data:
        if data[0].get("Phone", None) == "123":
            return Response("3", mimetype="text/plain")  # solid rng
        else:
            return Response("2", mimetype="text/plain")


def message_get_list() -> Response:
    data = request.get_json(silent=True)  # type: dict

    if data:
        if isinstance(data, dict):
            max_limit = 20

            # noinspection PyShadowingBuiltins
            id = data.get("ID", "")
            start = data.get("Start", 0)
            limit = data.get("Limit", max_limit)

            with open("resources/test/message_get_latest.txt", "r") as f:
                json_file_data = json.load(f)  # type: typing.List[dict]

            obj_filter = filter(lambda o: o["ID"] == id, json_file_data)

            try:
                obj = next(obj_filter)
            except StopIteration:
                return Response("[]", mimetype="text/plain")

            objs = [obj]

            if start <= 0:
                limit = max_limit - 1 if limit > max_limit - 1 else limit - 1
            else:
                del objs[0]
                limit = max_limit - start if limit > max_limit \
                    else limit

            for i in range(limit):
                the_chosen_one = random.choice(json_file_data)
                objs.append(the_chosen_one)

            response_data = json.dumps(objs)
            response = Response(response_data, mimetype="text/plain")
        else:
            response = Response("", mimetype="text/plain")
    else:
        response = Response("", mimetype="text/plain")

    return response


groups = []  # type: typing.List[dict]


def contact_group_get_list() -> Response:
    global groups
    if not groups:
        with open("resources/test/contact_group_get_list.txt", "r") as f:
            groups = json.loads(f.read())

    response = Response(json.dumps(groups), mimetype="text/plain")

    return response


def contact_add_group() -> Response:
    global groups  # type: typing.List[dict]

    def get_next_id() -> int:
        ids = [g["ID"] for g in groups]
        return max(ids)+1

    group_name = str(
        request.get_json(silent=True)[0]["GroupName"]
    )  # type: str
    # noinspection PyShadowingBuiltins
    id = get_next_id()

    group_data = {
        "ID": id,
        "GroupName": group_name,
        "AccountName": "baz",
        "AccountType": "pyairmore"
    }

    groups.append(group_data)

    response_data = group_data.copy()

    response_data.pop("AccountType")
    response_data.pop("AccountName")

    return Response(json.dumps([response_data]), mimetype="text/plain")


@app.route('/', methods=["GET", "POST"])
def path():
    arg = request.args.get("Key", None, str)

    with open("resources/test/home.txt", "r") as f:
        default_response = f.read()

    responses = (
        ("PhoneCheckAuthorization",
         lambda: Response('"0"', mimetype="text/plain")),
        ("PhoneRequestAuthorization",
         lambda: Response("true", mimetype="text/plain")),
        ("PhoneGetDeviceInfo", get_device_info),
        ("PhoneRefreshScreen", refresh_screen),
        ("MessageGetLatest", message_get_latest),
        ("MessageSend", message_send),
        ("MessageGetList", message_get_list),
        ("ContactGroupGetList", contact_group_get_list),
        ("ContactAddGroup", contact_add_group),
    )  # type: typing.Tuple[typing.Tuple[str, callable]]

    for response in responses:
        if arg == response[0]:
            res = response[1]()

            if res:
                return res

    return Response(default_response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(port=2333)
