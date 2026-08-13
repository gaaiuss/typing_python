from collections.abc import Callable
from resource.utils import cyan_print, sep_print

sep_print()


# Typing functions
def remove_duplicates(items: list[str]) -> list[str]:
    # dict.fromkeys generates a dictionary from a list
    to_dict = dict.fromkeys(items)
    # list converts dict to list, remove duplicates and keep the order
    return list(to_dict)


duplicates_list = ["a", "a", "a", "b", "b", "c", "123", "123", "Caio"]
unique_items = remove_duplicates(duplicates_list)
cyan_print(f"{unique_items=}")
sep_print()


def is_image_file(filename: str) -> bool:
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    name_lower_case = filename.lower()

    return name_lower_case.endswith(extensions)


# Usage
filename = "file.exe"
cyan_print(f"{is_image_file(filename)=} | {filename=}")
filename = "image.JPEG"
cyan_print(f"{is_image_file(filename)=} | {filename=}")
filename = "photo.png"
cyan_print(f"{is_image_file(filename)=} | {filename=}")
filename = "meme.gif"
cyan_print(f"{is_image_file(filename)=} | {filename=}")

sep_print()

# Callables
# What is a callable? Everything that you execute:
# - Functions (def)
# - Methods (functions inside classes)
# - Classes itselves (to create instances)
# - Objects that implements the speacial method '__call__'


# Callable [args, return]
# Example Callable [[str, bool, int], None]
# Example Callable [..., int]
def with_callback(x: float, y: float, callback: Callable[..., None]) -> float:
    result = x + y
    callback(f"{result=}")
    return x + y


with_callback(2, 5, cyan_print)
sep_print()


def with_args(*args: str) -> None:
    cyan_print(*args)


with_args("Oi,", "tudor", "bem?")
sep_print()


def with_kwargs(*args: int, **kwargs: str) -> None:
    cyan_print(f"{args=}")
    cyan_print(f"{kwargs=}")


with_kwargs(1, 2, 3, name="Galior", surname="Prime")
sep_print()
