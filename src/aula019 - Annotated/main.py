"""Annotated

Metadata: Data that describes other data. Like images description (image metadata),
python modules, functions, classes, etc.

Annotated: Parametrized type used to add metadata on another types. You are
creating another type and adding parameters to it.
"""

from dataclasses import dataclass
from resource.utils import cyan_print as p
from resource.utils import sep_print as s
from typing import Annotated, get_args, get_origin, get_type_hints

# In this casa for all the linters `integer` is a int type and for the second
# argument foward you can add any metadata you want.
integer: Annotated[int, "A integer number"]

"""
For the parameters you can use it to anything that you can imagine: docs, 
validation, refactor, etc.

The most interesting part is that you can use the metadata in runtime as other
libs already use: Pydantic, FastAPI, Langchain e Langgraph.

You can only use Annotated with classes, functions, modules and objects.

Functions that are commonly used with Annotated:

- get_type_hints: Return the typing data of a function, method, class, etc.
- get_args: Return the internal arguments of the Annotated.
- get_origin: Return the external type, 'Annotated'.
"""


# As explained before an Annotation can only be used by a container like a class
# or in this case a function
def simple_annotation(
    annotated: Annotated[object, "I have annotation"],
) -> Annotated[object, "I have annotation"]:
    return annotated


s()

# `include_extras=False` this comes by default and it does as explained before
# hides all the metadata and returns only the types
type_hints = get_type_hints(simple_annotation, include_extras=False)
p(f"{type_hints=!r}")
s()

# You can set this to show the metadata but it is not very usable as you do not
# have access to each parameter:
type_hints = get_type_hints(simple_annotation, include_extras=True)
p(f"{type_hints=!r}")
s()
# returns:
# {
#     'annotated': typing.Annotated[object, 'I have annotation'],
#     'return': typing.Annotated[object, 'I have annotation']
# }

# Right here we will get the args of each key of the type hints showed atop with
type_args = get_args(type_hints["annotated"])
type_return = get_args(type_hints["return"])

p(f"{type_args=!r}")
p(f"{type_return=!r}")

# Here we will get the external element which is the type Annotated the comes
# before the args
type_origin = get_origin(type_hints["annotated"])
p(f"{type_origin=!r}")

s()


# Example with a dataclass
@dataclass
class Person:
    """A person object"""

    # In this case I could use the metadata of these elements to create a doc
    name: Annotated[str, "The full name of a person"]
    age: Annotated[int | None, "The age"] = None


# Example to check the metadata in runtime
def print_annotated[T: object](obj: T) -> T:
    obj_class = obj.__class__
    obj_name = getattr(obj, "__name__", "")

    if not obj_name:
        obj_name = obj_class

    # Get Annotation data: Annotated[type, metadata]
    # `include_extras=True` to get the metadata
    hints = get_type_hints(obj, include_extras=True)

    # If no hints present just return the object
    if not hints:
        return obj

    # Now we will print everything
    p("Verifying typing of:", obj_name)
    p(f"Real Object: {obj=!r}")

    for key, value in hints.items():
        # `get_args` will return the type and the rest of what is inside of
        # Annotated
        type_, *metadata = get_args(value)

        p(f"Key={key!r}, Type={type_!r}, Metadata={metadata!r}")

    p()
    s()

    return obj


print_annotated(simple_annotation)

person = Person("Caio", 26)
print_annotated(person)
