# Generict types inside collections abc
# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/stdtypes.html#standard-generic-classes

# "Be liberal in what you accept, and conservative in what you return."

# Generics: types that receives other parameters


from collections.abc import Callable, Iterable
from resource.utils import cyan_print, sep_print

from aula003.main import Animal, Cat, Tiger


# This could be done but it is impractical for you would need to write every
# type manually using Union (|)
# def concat(items: list[str] | set[str] | str) -> str:
# Instead we use a more generic class to accept as many iterables as possible
def concat(items: Iterable[str]) -> str:
    return "".join(items)


letters_list = ["a", "b", "c"]
letters_set = {"a", "b", "c"}
letters_str = "abc"
letters_tuple = ("a", "b", "c")
letters_dict = {"a": None, "b": False, "c": 123}

sep_print()

cyan_print(f"{concat(letters_list) = !r}")
cyan_print(f"{concat(letters_set) = !r}")
cyan_print(f"{concat(letters_str) = !r}")
cyan_print(f"{concat(letters_tuple) = !r}")
cyan_print(f"{concat(letters_dict) = !r}")

sep_print()

# ------------------------------- Covariance ---------------------------------

# Basically is a subtype relation: boolean is a subtype of int, so that is a
# covariant realation

type C[T] = tuple[T, ...]

integers: C[int] = 1, 0, 1, 0
booleans: C[bool] = True, False, True, False

# booleans = integers # Does not work
integers = booleans  # Works because booleans is a subtype


# ----------------------------- Contravariant --------------------------------

# Contrary to the subtype relation, it follows the reverse path and it is used
# on Callables


def animal_handler(obj: Animal) -> None: ...
def cat_handler(obj: Cat) -> None: ...
def tiger_handler(obj: Tiger) -> None: ...


def handle(cat: Callable[[Cat], None]) -> None: ...


# When you need a specific task to be done, only a specialist on that task or
# a more abrangent specialist can handle that task
handle(cat_handler)
handle(animal_handler)

# Does not work because a tiger specialist can only handle tigers and not cats
# in general
# handle(tiger_handler)


# ----------------------------- Invariance ----------------------------------

# Appears in mutable types: list, set, dict


# In this function I want a list of str or int.
# We can imagine that list[str | int] would accept:
# a list of str
# a list of int
# a list of int and str
# But NO! Only a list of str AND int (Invariance)
def handle_str_int(items: list[str | int]) -> None: ...


my_list: list[str] = ["a", "b"]
# handle_str_int(my_list)  # Type checker error

# This would mean that if list is mutable, the function could add a int on it
# and change the type o the list stealthly. In the end'my_list' would become a
# list[str | int] breaking another locales in the program.


def handle_str_int_imutable(items: tuple[str | int, ...]) -> None: ...


my_tuple: tuple[str, ...] = "a", "b"
# This works because tuple is imutable, so the risk of it changing its type
# does not exists like in the list case.
handle_str_int_imutable(my_tuple)
