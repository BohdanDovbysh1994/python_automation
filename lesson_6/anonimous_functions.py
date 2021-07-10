def some_1(a, b, c):
    result = a + b + c
    return result


some_2 = (
    lambda a, b, c:
    a + b + c
)


# print((lambda a, b, c: a + b + c)(1, 2, 3))

if __name__ == '__main__':
    some_2(1, 2, 3)
