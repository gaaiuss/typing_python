from collections.abc import Callable

from rich.console import Console

console = Console(markup=True, log_path=False, log_time=False)
rprint = console.log


def make_print(style: str) -> Callable[..., None]:
    def fake_print(*values: object) -> None:
        return console.log(*values, style=style)

    return fake_print


def sep_print() -> None:
    rprint(f"\n{80 * '-'}\n", style="yellow")


cyan_print = make_print(style="cyan")
