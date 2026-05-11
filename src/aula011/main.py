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

from typing import Protocol


class SupportsRead[Out](Protocol):
    def read(self) -> Out: ...


class SupportsWrite[In](Protocol):
    def write(self, data: In) -> None: ...


class SupportsReadWrite[In, Out](SupportsRead[Out], SupportsWrite[In], Protocol): ...
