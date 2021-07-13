from typing import List

names = ["John", "Marta"]


def update_name(names_list: List[str]):
    names_list.append("OLOLO")


def outer():
    def inner():
        return "World"
    print("Hello")

    return inner


if __name__ == '__main__':
    print(outer()())
