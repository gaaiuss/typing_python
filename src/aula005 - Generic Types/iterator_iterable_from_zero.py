# Iterable: An object that can return its elements one at a time or an object
# you can loop over. It implements __iter__(). Examples: list, tuple, str, dict, set
#
# Iterator: object that produces values one at a time during iteration.
# __iter__() → returns itself
# __next__() → returns next item (or raises StopIteration)


from resource.utils import cyan_print, sep_print
from typing import Self


class MyList:
    def __init__(self) -> None:
        self.__data: dict[int, object] = {}
        self.__index = 0
        self.__next_index = 0

    def add(self, *values: object) -> None:
        for value in values:
            self.__data[self.__index] = value
            self.__index += 1

    def __check_index(self, index: int) -> None:
        if not self.__data.get(index):
            msg = f"Index '{index}' does not exists."
            raise IndexError(msg)

    def __setitem__(self, index: int, value: object) -> None:
        self.__check_index(index)
        self.__data[index] = value

    def __getitem__(self, index: int) -> object:
        self.__check_index(index)
        return self.__data[index]

    def __delitem__(self, index: int) -> None:
        self.__data[index] = None

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> object:
        if self.__next_index >= self.__index:
            self.__next_index = 0
            raise StopIteration

        value = self.__data.get(self.__next_index)
        self.__next_index += 1
        return value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.__data})"


if __name__ == "__main__":
    my_list = MyList()

    sep_print()

    my_list.add("Caio", "Silva")
    my_list.add("G")
    my_list.add("C")

    my_list[0] = "Gaius"

    # delete item
    # del my_list[0]

    # simulate erros
    # cyan_print(my_list[10])

    # using for
    for item in my_list:
        cyan_print(item)

    sep_print()

    cyan_print(my_list)

    sep_print()
