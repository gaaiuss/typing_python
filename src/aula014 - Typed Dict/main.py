"""TypedDict

To reduce the possibilities of a normal dict typing, like:
mydict: dict[A | B, C | D] = {...}, where we create a good amount of possibilities
(cartesian product), we use instead TypedDict with a more precise typing
approach.
"""

from resource.utils import cyan_print, sep_print
from typing import NotRequired, ReadOnly, Required, TypedDict


# `total`means that all the keys must be or not be present. Total can be ommited
#  as it is default True
class MyDict(TypedDict, total=True):  # total=False - Keys can be optional
    id: int
    name: Required[str]  # as the `total` is explicit True, Required here is redundant
    email: Required[str]
    gender: NotRequired[str]  # keys can be optional by expecifying NotRequired
    birth: Required[ReadOnly[str | None]]  # ReadOnly: this key cannot change


"""This is another way of creating a TypedDict. The advantage of this is that
you can use special characters an even python exclusive keywords"""
NiceDict = TypedDict(
    "NiceDict",
    {
        "first-name": str,  # Minus on key
        "last-name": NotRequired[str],
        "birth-year": int,
        "in": NotRequired[bool],  # Python exclusive keyword
        "__it-works": str | None,  # dunder (Not a good pratice for keys)
    },
)


if __name__ == "__main__":
    sep_print()

    my_dict: MyDict = {
        "id": 123,
        "name": "Caio G",
        "email": "caiog@gmail.com",
        # "gender": "Male",  # NotRequired
        "birth": "30/06/2000",  # Optional: str or None
    }

    cyan_print(my_dict["id"])
    sep_print()
