from resource.utils import cyan_print, sep_print

sep_print()


# Typing functions
def remove_duplicates(items: list[str]) -> list[str]:
    # dict.fromkeys generates a dictionary from a list
    to_dict = dict.fromkeys(items)
    # list converts dict to list, remove duplicates and keep the order
    return list(to_dict)


duplicates_list = ["a", "a", "a", "b", "b", "c", "123", "123", "Caio"]
unique_items = remove_duplicates(duplicates_list)
cyan_print(f"{unique_items=}")
sep_print()
