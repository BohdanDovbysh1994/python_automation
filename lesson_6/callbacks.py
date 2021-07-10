from typing import Callable


def custom_sum(a: int, b: int) -> int:
    return a + b


def custom_difference(a: int, b: int) -> int:
    return a - b


def do_action(callback: Callable, a: int, b: int):
    return callback(a, b)


if __name__ == '__main__':
    print(do_action(custom_sum, 2, 4))
    print(do_action(custom_difference, 2, 4))