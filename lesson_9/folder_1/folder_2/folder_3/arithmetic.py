from .. import devide


def sum(a, b):
    return a + b


def difference(a, b):
    return a - b


def multiply(a, b):
    return a * b


def some_dich():
    devide(1/0)


if __name__ == '__main__':
    print(sum(2, 2))
