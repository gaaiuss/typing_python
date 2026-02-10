# Basic types (Implicit and Explicit)
# Implicit types change to Literal (the value itself) and can be type
# chaged if not expecified, explicit types as
# informed below can't change their types in the entirety of the code
from typing import Final

name: str = "Caio"
x: int = 11
y: float = 23.22
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b"whatever"

# Constants
# Constants already are Literal by convention, changing it are redundant and
# can cause problems later
CONSTANT = "constant value"

# Collections
number_list: list[int] = [1, 2, 3]
two_value_tuple: tuple[str, int] = ("value", 234)
various_tuple: tuple[str, ...] = "a", "b", "c", "..."
sets: set[int] = {1, 2, 3, 4}
immutable_set: frozenset[int] = frozenset([2, 3, 4, 5])
dictionary: dict[str, str] = {"key": "value", "key2": "value2"}
numbers: range = range(10)

# Other types
none_var: None = None  # represents absence of value
anything: object = "123"  # can be any object
type_var: type[str] = str  # reference to a type itself

# Constants again
# Final explicits a constant variable
CONSTANT2: Final[list[str]] = ["a", "b"]
contant3: Final[dict[str, int]] = {"number": 123, "another_number": 234}
