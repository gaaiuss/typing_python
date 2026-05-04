# Type vars and generic functions

# Type var is a type parameter that acts as a unknown symbol to act as a yet
# unknown type. Its value will be replaced by a concrete type during the static
# verificaqtion or the type inference


from collections.abc import Hashable, Iterable, MutableMapping, Sequence
from resource.utils import cyan_print, sep_print


# Filters a iterable by type. The iterable can have any type inside it
def filter_by_type[T](items: Iterable[object], type_: type[T]) -> list[T]:
    return [item for item in items if isinstance(item, type_)]


def reverse_in_groups[T](items: Sequence[T], group_size: int = 2) -> list[T]:
    return [
        group
        for index in range(0, len(items), group_size)
        for group in reversed(items[index : index + group_size])
    ]


# O hash do dicionário é um número calculado pelo __hash__ que serve como
# identificador rápido do conteúdo de algumas estruturas de dados como
# dict e set.
# O hash nunca deve mudar, por isso os valores para a chave precisam ser imutáveis.
def invert_mapping[K, V: Hashable](m: MutableMapping[K, V]) -> MutableMapping[V, K]:
    return {value: key for key, value in m.items()}


if __name__ == "__main__":
    sep_print()

    mixed = [1, 2, 3, "a", "b", "c", {10, 20, 30}]
    filtered = reverse_in_groups(mixed, group_size=3)
    cyan_print(mixed)
    cyan_print(filtered)

    sep_print()

    dict1 = {
        "a": 1,
        "b": 2,
        (1, 2): 3,
    }
    invert = invert_mapping(dict1)
    revert = invert_mapping(invert)

    cyan_print(dict1)
    cyan_print(invert)
    cyan_print(revert)

    sep_print()
