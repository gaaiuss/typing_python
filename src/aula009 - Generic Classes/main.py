# Generic classes

# The generic class typing or generic classes follows the same pattern of the
# generic functions of the previous lesson. Define a type parameter on the class
# and it automatically becomes a generic class with the new syntax of PEP 695

# In the following example we have a MutableMapping that is fixed with a key and
# value. Our work here is to turn that into a generic class that accepts type
# parameters so that it can be used with the types that achieve the objective.

# The final objective is to achive the possibility to invert the kye and value.
# Remember that the key must be hashable.

from collections.abc import Hashable, Iterable, Iterator, Mapping, MutableMapping
from resource.utils import cyan_print, sep_print


class MyMutableDict[K: Hashable, V: Hashable](MutableMapping[K, V]):
    def __init__(self, data: Mapping[K, V] | Iterable[tuple[K, V]]) -> None:
        self._data: dict[K, V] = dict(data)

    # You cannot invert this dict. You must return [int, str], but the class
    # only accepts [str, int]
    def inv(self) -> MutableMapping[V, K]:  # This return can be restrict
        inverted = ((v, k) for k, v in self._data.items())  # generator comprehension
        return MyMutableDict(data=inverted)

    # Same idea, there is no way to invert [str, int] and [int, str]
    def inv_strict(self) -> MutableMapping[V, K]:
        inverted: MutableMapping[V, K] = {}

        for k, v in self._data.items():
            if v in inverted:
                msg = f"Key={v!r} is not allowed because {v!r} is a key duplication"
                raise KeyError(msg)

            inverted[v] = k

        return MyMutableDict(data=inverted)

    def __iter__(self) -> Iterator[K]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, key: K) -> V:
        return self._data[key]

    def __setitem__(self, key: K, value: V) -> None:
        self._data[key] = value

    def __delitem__(self, key: K) -> None:
        del self._data[key]

    def __repr__(self) -> str:
        attrs = [f"{k}={v!r}" for k, v in self._data.items()]
        cls_name = type(self).__name__
        return f"{cls_name}({', '.join(attrs)})"


if __name__ == "__main__":
    data1 = ("key1", 1), ("key2", 2), ("key3", 3)
    # These two could not be used with my mapping
    data2 = (1, "key1"), (2, "key2")
    data3 = (1, (1, 2, 3)), (2, [4, 5, 6])

    my_dict = MyMutableDict(data=data1)
    my_dict2 = MyMutableDict(data=data2)
    # my_dict3 = MyMutableDict(data=data3)

    sep_print()

    cyan_print(my_dict)
    cyan_print(my_dict.inv())
    cyan_print(my_dict.inv_strict())
    cyan_print()
    cyan_print(my_dict2)
    cyan_print(my_dict2.inv())
    cyan_print(my_dict2.inv_strict())
    # cyan_print()
    # cyan_print(my_dict3)
    # cyan_print(my_dict3.inv())
    # cyan_print(my_dict3.inv_strict())

    sep_print()
