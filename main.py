from rich.console import Console
from typeguard import typechecked

@typechecked
class Formatter:
    def bold_green(self, text: str) -> str:
        return f"[bold green]{text}[/green bold]"

if __name__ == "__main__":
    console = Console()
    formatter = Formatter()
    console.print(formatter.bold_green("Hello, World!"))