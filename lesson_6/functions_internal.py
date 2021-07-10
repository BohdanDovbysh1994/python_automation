from typing import Callable


def get_name() -> Callable:
    def some_dich(first_name: str) -> str:
        return f"{first_name} Dow"

    return some_dich


if __name__ == '__main__':
    print(get_name()("John"))
