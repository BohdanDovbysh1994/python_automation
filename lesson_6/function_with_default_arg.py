from typing import Optional


def some(name: str, age: Optional[int] = 32) -> str:
    return f"{name} {age}"


if __name__ == '__main__':
    print(some("John", 23))
