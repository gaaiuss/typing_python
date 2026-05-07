# Protocol and Structural Subtyping: static typing in Python

# Until now we have been working with nominal typing, in other words, a class
# is subtype of another only when you declare it explicitly.
# Example: if 'B' inherit from 'A', then 'B' is an 'A'. This is nominal subtyping.

# In daily life, Python is famous by the 'duck typing', in other words, in runtime
# Python is not checking inheritance but instead a if especific method or attribute
# exists in the project.

# The good news is that in the static typing we also have an equivalent of duck
# typing and that is Structural Typing.

# To work with structural typing we use Protocol. It permits us to define a 'contract'
# of methods/atributes that any class can fulfill even without declaring inheritance

# Just as in ABC, the 'contract' is nominal and has its effect during runtime
# (SUbclass without abstract method cannot be instantiated).

# With Protocol, the contract is structural and works mainly in static, the type
# checker accepts any object with the correct 'form'. In runtime, protocol is a
# special class, but cannot validate implementations by itself.

# https://typing.python.org/en/latest/reference/protocols.html#predefined-protocol-reference

from dataclasses import dataclass
from resource.utils import cyan_print, sep_print
from typing import Protocol


class SupportsTalk(Protocol):
    name: str

    def talk(self, phrase: str) -> None: ...


@dataclass
class Person:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


@dataclass
class Toy:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


def talk(obj: SupportsTalk, phrase: str) -> None:
    cyan_print(f"{obj.__class__.__name__}({obj.name}) will talk")
    obj.talk(phrase)


if __name__ == "__main__":
    sep_print()

    person1 = Person("Caio")
    toy1 = Toy("Buzz Lightyear")

    talk(person1, "I know how to talk.")
    talk(toy1, "I know how to talk.")

    sep_print()
