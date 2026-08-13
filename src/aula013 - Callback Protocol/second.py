# Typevar with callback protocol

import re
from resource.utils import cyan_print, sep_print
from typing import Protocol

################################################################################
#
# It is possible as well to use `Typevar` with protocols. This allow you to do
# signature in your function in a more dynamic way. So, the types can variate
# accordingly with the context.
# In the example bellow, we have a very simple Protocol. The intention is to
# receive a named attribute called `value` with a type `T` and return `R`.
# Both `T` and `R` are `Typevars` or dynamic Type Parameters.
################################################################################

# This regular expression will be used to clean commas.
# It selects the following:
# - `\s*` - zero or more spaces
# - `,` - comma
# - `\s*` - zero or more spaces
# Free regex course:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr
RE_COMMA_SPACE = re.compile(r"\s*,\s*")


################################################################################

# We are going to define the `Protocol` that accepts all the parameterizied types
# (`TypeVar`)


class TypeCaster[T, R](Protocol):
    def __call__(self, *, value: T) -> R: ...


################################################################################

# Now we can define our functions that fulfill the contract


def to_str(*, value: object) -> str:
    """Receives anything and converts to string"""

    return str(value)


def str_to_list(*, value: str) -> list[str]:
    """Receives a string and tries to convert into list"""

    clean_value = RE_COMMA_SPACE.sub(value, ",")
    return [v.strip() for v in RE_COMMA_SPACE.split(clean_value) if v.strip()]


def wrong_kw_name(text: str) -> str:
    """❌ This named argument is wrong named"""

    return text


################################################################################

# Finally, we are going to define something that "uses" our `Protocol` and test
# if our functions pass in the typing. Note that here we are really using our
# functions as callbacks (making the name callback protocol worth).


def run_type_caster[T, R](value: T, type_caster: TypeCaster[T, R]) -> R:
    """Receives a value, a type caster and executes everything"""

    return type_caster(value=value)


################################################################################

# Let us test everything

if __name__ == "__main__":
    value_to_str = run_type_caster([1, 2, 3], to_str)
    value_to_list = run_type_caster(
        ",,,,abc,,,def,Caio Guilherme, a, b,c ,,,",
        str_to_list,
    )

    # This does not only typing error but also in runtime
    # wrong_callback = run_type_caster("", wrong_kw_name)  # ❌

    # Here I am trying to send a `int` to a callback that waits for a `str`
    # Also generates both typing and runtime error
    # wrong_argument = run_type_caster(123, str_to_list)  # ❌

    sep_print()

    cyan_print(f"{value_to_str = }")
    cyan_print(f"{value_to_list = }")
    # cyan_print(f"{wrong_kw_name = }")  # ❌
    # cyan_print(f"{wrong_argument = }")  # ❌

    sep_print()
