def factorial_recursive(n: int):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    pass