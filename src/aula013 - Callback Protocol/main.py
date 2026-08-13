# Callback Protocol vs Callable
from collections.abc import Callable
from resource.utils import cyan_print, sep_print
from typing import Protocol

# Tell me what is it?
type ReallyRelaxedCallable = Callable[..., None]  # (*args, **kwargs) -> None

# And this?
type MysticCallable = Callable[[int, int, str], bool]  # (1, 2, 'a') -> true

# We can assume that:
# `ReallyRelaxedCallable` receives anything and returns `None`.
# `MysticCallable` receives `int`, `int` e `str` e returns `bool`.

################################################################################
#
# There is nothing wrong using `Callable`, in fact, we are going to use them
# Much more than `Protocols`.
# Although, at some point, the name of the arguments will matter. Maybe you
# will create a function that only can recive named arguments or that can have
# a very complex signature.
# In these cases, callback protocols resolve the problem.
# With them it is possible to define a contract through a protocol and after
# do whatever you want with the `__call__` method.
#
################################################################################


# Callback protocol is very easy to implement.


class CallbackProtocol(Protocol):
    # You just need to define the signature of your function in the `__call__`
    # method.
    # Please, never forget the `self`.
    def __call__(self, *, whatever: str) -> str: ...


################################################################################

# Functions to test: one have the right signature, the other do not.


def good_func(*, whatever: str) -> str:
    """This function fulfills the contract ✅"""
    return whatever


def bad_func(not_good: str) -> str:
    """This function DO NOT fulfills the contract ❌"""
    return not_good


################################################################################

# Let us test all together

if __name__ == "__main__":
    sep_print()

    # 🧐 This is for the obssessed for types. It is not necessary.
    # Generally, we are going to use callback protocol with... guess? [callbacks]
    # But, this will serve to our first example without complexing things.
    good: CallbackProtocol = good_func
    bad: CallbackProtocol = bad_func

    # Let us use functions
    same_str_good = good(whatever="Here is your string back")
    same_str_bad = bad(not_good="Here is your string back")

    # Python does not care (as always)
    cyan_print(f"{same_str_good}")  # Python ✅
    cyan_print(f"{same_str_bad}")  # Python ✅

    sep_print()


################################################################################
