from typing import Union, Callable


def do_action(callback: Callable, a: int, b: int) -> Union[int, float, str]:
    return callback(a, b)


def make_difference(c: int, d: int) -> int:
    return c - d


def make_sum(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(do_action(make_sum, 5, 5))
    print(do_action(make_difference(5, 6), 10, 15))
