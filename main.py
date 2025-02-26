import os
from typing import Any, Callable
from rich.console import Console


if os.getenv("ENABLE_TYPEGUARD", "1") == "1":
    from typeguard import typechecked
else:
    # Define a no-op decorator
    def typechecked(func: Callable[..., Any]) -> Callable[..., Any]:
        return func

@typechecked
class Formatter:
    def bold_green(self, text: str) -> str:
        return f"[bold green]{text}[/green bold]"

if __name__ == "__main__":
    console = Console()
    formatter = Formatter()
    console.print(formatter.bold_green("Hello, World!"))