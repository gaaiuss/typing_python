# Generict types inside collections abc
# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/stdtypes.html#standard-generic-classes

# "Be liberal in what you accept, and conservative in what you return."

# Generics: types that receives other parameters


from collections.abc import Iterable
from resource.utils import cyan_print, sep_print


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

# Covariance and Contravariance in standard generics

# A covariant collection or container is intuitive
