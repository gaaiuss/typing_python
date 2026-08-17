"""Discriminated Union

Typing based on a determined value is possible with discriminated union. In this
typing method, we generate a tag in a determined key and decide the typing structure
based on this tag.

Imagine a server response case, it can return many response variations (OK, error),
and for each response case, it return a different key/value.
"""

from resource.utils import cyan_print, green_print, red_print, sep_print
from typing import Literal, TypedDict


class ResponseSuccess(TypedDict):
    status: Literal["ok"]  # this is the tag
    data: str  # just an example for simplicity purpose


class ResponseError(TypedDict):
    status: Literal["error"]  # tag
    message: str  # just an example for simplicity purpose


type Response = (
    ResponseSuccess | ResponseError  # discriminated union with the `status` tag
)


def handle_response(res: Response) -> None:
    match res["status"]:
        case "ok":
            green_print("RESPONSE OK", res["data"])
            return
        case "error":
            red_print("ERROR", res["message"])
            return

    red_print("I can't handle this response.")


if __name__ == "__main__":
    sep_print()

    response_success: ResponseSuccess = {"status": "ok", "data": "Here is your result"}
    handle_response(response_success)
    cyan_print()
    sep_print()

    response_error: ResponseError = {"status": "error", "message": "BadRequest"}
    handle_response(response_error)
    cyan_print()
    sep_print()

    wrong_reponse = {"status": "any"}
    handle_response(wrong_reponse)
    cyan_print()
    sep_print()
