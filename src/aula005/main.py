from resource.utils import cyan_print, sep_print


def concat(items: list[str] | set[str] | str) -> str:
    return "".join(items)


letters_list = ["a", "b", "c"]
letters_set = {"a", "b", "c"}
letters_str = "abc"
letters_tuple = ("a", "b", "c")
letters_dict = {"a": None, "b": False, "c": 123}

sep_print()

cyan_print(f"{concat(letters_list)} = !r")
cyan_print(f"{concat(letters_set)} = !r")
cyan_print(f"{concat(letters_str)} = !r")
cyan_print(f"{concat(letters_tuple)} = !r")
cyan_print(f"{concat(letters_dict)} = !r")

sep_print()
