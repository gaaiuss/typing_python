# Classes


from resource.utils import cyan_print, sep_print


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def talk(self) -> None:
        raise NotImplementedError


class Cat(Animal):
    def talk(self) -> None:
        cyan_print(f"{self.name!r} says 'miau!'")
        sep_print()


def get_animal_name(animal: Animal) -> None:
    cyan_print(f"'get_animal_name' | Classe: {type(animal).__name__}")
    cyan_print(f"'get_animal_name' | {animal.name = !r}")
    sep_print()


if __name__ == "__main__":
    cat = Cat("Sina")

    sep_print()
    get_animal_name(cat)

    # Lets talk
    cat.talk()
