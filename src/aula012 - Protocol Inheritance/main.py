# Inheritance with Protocols

# As it is not good to use Protocols as Abstract classes, it is important to know
# that you can make them act in a simillar way

# The benefits:
#  - You do not need to write your code in the dark (the typing will help you)
#  - You gain any concrete implementation of Protocol
#  - You can define abstract methods that generate errors in runtime

# Obs.: we have basically an ABC here without the typing benefits we have talked
# about (isinstance, issubclass, etc...)

# https://youtu.be/-nSOKE4f2gA?si=Ds1TBFhcU0iYS0U0

# Python Doc
# https://typing.python.org/en/latest/spec/protocol.html#protocols
from abc import abstractmethod
from resource.utils import cyan_print, sep_print
from typing import Protocol, final


class TemplateMethod[A, B](Protocol):
    @abstractmethod  # this is going to generate runtime error
    def step_a(self) -> A: ...
    @abstractmethod
    def step_b(self) -> B: ...

    @final
    def run(self) -> tuple[A, B]:
        result_a = self.step_a()
        result_b = self.step_b()

        return result_a, result_b


class MakePair[T](TemplateMethod[T, T]):
    def __init__(self, a: T, b: T) -> None:
        self.a = a
        self.b = b

    def step_a(self) -> T:
        return self.a

    def step_b(self) -> T:
        return self.b


if __name__ == "__main__":
    sep_print()
    pair_maker = MakePair("Joãozinho", "Maria")
    pair = pair_maker.run()
    cyan_print(pair, f"{pair[0]} {pair[1]}")
    sep_print()

    pair_maker = MakePair[tuple[int, int]]((1, 2), (3, 4))
    pair_a, pair_b = pair_maker.run()
    cyan_print(pair_a, pair_b, sum(pair_a + pair_b))
    sep_print()
