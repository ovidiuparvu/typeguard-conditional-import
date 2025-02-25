from typeguard import typechecked

@typechecked
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

if __name__ == "__main__":
    say_hello("John")