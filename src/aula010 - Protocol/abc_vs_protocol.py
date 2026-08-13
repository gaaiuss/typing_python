# ABC vs Protocol

# Protocol is very similar to ABC but there are differences that change the choice:

# ABCs -> Nominal contract with runtime effect. You need to inherit from ABC;
# classes that do not implement the abstracts do not instantiate. Beyond that,
# isinstance/issubclass work normally.

# Protocols -> Structural contract imagined to work with the type checker. You
# do not need to inherit, the correct form is enough (methods, compatible attributes).
# In runtime, Protocol does not validates implementations by itself. If you want
# to check in runtime, use @runtime_checkable, it only checks if the attribute
# exists, the signature does not reach 100%.

# Mental note:
#  - You need to impose a rule in runtime via inheritance? -> ABC.
#  - You want to accept who has the correct form without nominal attachment? -> Protocol

from abc import ABC, abstractmethod
from resource.utils import cyan_print, sep_print
from typing import Protocol, runtime_checkable


class ShapeAbc(ABC):
    @property
    @abstractmethod
    def area(self) -> float: ...


@runtime_checkable
class ShapeProtocol(Protocol):
    # In Protocol you do not need @abstractmethod; the type checker already
    # treat it as a contract
    @property
    def area(self) -> float: ...


class MyShapeAbc(ShapeAbc):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.x * self.y


class MyShapeProtocol:
    @property
    def area(self) -> float:
        return 1.1


def wants_shape_abc(shape: ShapeAbc) -> None:
    cyan_print(shape.area)


def wants_shape_protocol(shape: ShapeProtocol) -> None:
    cyan_print(shape.area)


if __name__ == "__main__":
    sep_print()

    my_shape_abc = MyShapeAbc(10, 20)
    my_shape_protocol = MyShapeProtocol()

    wants_shape_abc(my_shape_abc)
    # wants_shape_abc(my_shape_protocol) # need to inherit from ShapeAbc

    wants_shape_protocol(my_shape_abc)  # reach by structure (has area -> float)
    wants_shape_protocol(my_shape_protocol)  # Idem

    sep_print()
