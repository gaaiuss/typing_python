# Many development principles in a basic code

# In this code we will aply all SOLID principles in a single turn. In a simple
# manner, you will understand all of then without using typing and nominal subtyping

from resource.utils import sep_print
from typing import Protocol


class SupportsRead(Protocol):
    path: str

    def read(self) -> object: ...


class JsonManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> dict[str, object]: ...  # this will be covariant


class CsvManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str: ...  # covariance again


def load_data(reader: SupportsRead) -> object:
    # reader as JsonManager or CsvManager, would be depending on something concrete
    # using protocol we are depending on a single abstraction:
    # This is called: Dependency inversion principle

    # Furthermore, protocol SupportsRead just have the method that it needs
    # This is another principle called: Interface Segregation Principle

    # Here we also have substitution: remember? Liskov Substitution principle?

    # By the way, maybe I also do not need to change this function at all:
    # therefore, Open Closed Principle.

    # Another one: this function have a single reason to change, SupportsRead.
    # We call this Single Responsibility Principle.

    # And with a short script, we implemented all SOLID.
    return reader.read()


if __name__ == "__main__":
    sep_print()

    json_data = load_data(JsonManager("file.json"))
    csv_data = load_data(CsvManager("file.csv"))

    sep_print()
