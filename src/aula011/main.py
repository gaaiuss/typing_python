# Protocol composition in Python: from ISP to structural typing

# You can compose protocols like 'lego blocks', in other words, it is possible to
# create various small protocols with a single behaviour and after unite these
# protocols into something bigger. This is a interesting concept to adept to the
# Interface Segregation Principle (ISP) from SOLID.

# Rules (Python Protocols):
#  - Inherit from ANY Protocol (without 'Protocol' on the list) creates a concrete class
#  - Inherit from a Protocol and include 'Protocol' on the list, creates a NEW
# protocol compound.
#  - You do not need to inherit from 'Protocol' to get structural typing
# (but makes it easier).
#  - @runtime_checkable (bellow)
#  - Attributes in protocols are invariants (mutables do not vary), prefer @property
#  - Protocols can be generic: 'Protocol[T]', contracts that vary with type.
#  - Composition of Protocols = multiple inheritance, sum of contracts (good for ISP).
#  - Great for arguments of method and functions (we are going to talk about
# that later).

# Using isinstance() with Protocols is not totally safe in runtime. For example,
# the signatures of the methods are not verified. The runtime checking only
# guarantees that the members of the protocol exist, not that they have the correct
# type. The issubclass() with protocols also only checks if methods exist, nothing more.
# https://typing.python.org/en/latest/reference/protocols.html#using-isinstance-with-protocols

# SOLID
# [S]ingle Responsibility Principle (SRP): a class can only have a single reason
#   to change.
# [O]pen/Closed Principle (OCP): software entities must be open to extension, but
#   closed to change.
# [L]iskov Substitution Principle (LSP): derived class objects must substitute objects
#   from the base class without breaking the program.
# [I]nterface Segregation Principle (ISP): is better to have various specific interfaces
#   than a single unique general interface.
# [D]ependency Inversion Principle (DIP): depend on only abstraction, not
#   implementation.

import json
from collections.abc import Callable
from pathlib import Path
from resource.utils import cyan_print, sep_print
from typing import Protocol


class SupportsRead[Out](Protocol):
    def read(self) -> Out: ...


class SupportsWrite[In](Protocol):
    def write(self, data: In) -> None: ...


class SupportsReadWrite[In, Out](SupportsRead[Out], SupportsWrite[In], Protocol): ...


class FileDataManager[Out](SupportsReadWrite[str, Out]):
    def __init__(self, path: Path, parser: Callable[[str], Out]) -> None:
        self.path = path
        self.parser = parser

    def read(self) -> Out:
        with self.path.open("r", encoding="utf-8") as file:
            data = file.read()

            return self.parser(data)

    def write(self, data: str) -> None:
        with self.path.open("w", encoding="utf-8") as file:
            file.write(data)


def manage_file[Out](file_manager: SupportsReadWrite[str, Out], data: str) -> Out:
    file_manager.write(data)
    return file_manager.read()


if __name__ == "__main__":
    sep_print()

    # Simple parser for int
    file_manager = FileDataManager(Path(".\\lesson11_a.txt"), int)
    data = manage_file(file_manager, "123")
    cyan_print(data, type(data))
    sep_print()

    # Parser JSON to list[int]
    file_manager = FileDataManager[list[int]](Path(".\\lesson11_b.txt"), json.loads)
    data = manage_file(
        file_manager,
        "[1,2,3,4]",  # JSON String NOT Python Literal
    )
    cyan_print(data, type(data))
    sep_print()

    # Parser JSON to dict[str, int]
    file_manager = FileDataManager[dict[str, int]](
        Path(".\\lesson11_c.txt"), json.loads
    )
    data = manage_file(
        file_manager,
        '{"a": 1, "b": 2}',
    )
    cyan_print(data, type(data))
    sep_print()
