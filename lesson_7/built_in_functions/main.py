"""Super module"""
from functools import reduce

names = ["John", "James", "Marta", "Marry", "Jane", "Alexander"]
salaries = [1000, 1500, 12, 200]
salary_2 = [0, 0, 0, 0, 1]
people = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(reduce(lambda a, b: a + b, salaries))
# print(reduce(lambda a, b: a * b, salaries))
# print(reduce(lambda a, b: a - b, salaries))
# print(reduce(lambda a, b: a / b, salaries))

# print(reduce(lambda name1, name2: name1 + " | " + name2, names))
# print(reduce(lambda list_1, list_2: list_1 + list_2, people))
# print(reduce(lambda a, b: a if a < b else b, salaries))  # min

# def my_max(seq: list):
#     max = 0
#
#     for item in seq:
#         if item > max:
#             max = item
#
#     return max
#
# print(reduce(lambda a, b, c: a if a > b else b, salaries))  # max



# print(
#     list(
#         zip(names, salaries)
#     )
# )

# print(abs(-60))
# print(all(salary))  # AND
# print(any(salary_2))  # OR
# print(bin(4))
# print(oct(4))
# print(hex(4))
# print(bool("1"))
# print(callable())
# print(chr(88))
# print(ord("X"))
# john = dict(age=45, name="John")
# print(john)
# print(dir(str))
# print(list(enumerate(names)))
# print(eval("1 / 0"))  # eval is evil

# print(
#     list(
#         filter(
#             lambda name: name.startswith('J'), names
#         )
#     )
# )

# print(globals())
# print(__name__)
# print(__doc__)
# print(__package__)
# print(hasattr("", "index-super"))
# name = input("Tell me your name: ")
# print(name)
# print(len("John"))

# print(globals())

# def fun(b: int):
#     a = 5
#     print(locals())
#
# fun(5)


# def update_name(name: str) -> str:
#     return f"Hello {name}"


# updated_salaries = list(
#     map(
#         lambda salary: salary + 100,
#         salaries
#     )
# )
# print(names)
# print(updated_names)

# print(salaries)
# print(updated_salaries)

# print(max(salaries))
# print(min(salaries))

# names_iterator = iter(names)
#
# print(next(names_iterator))
# print(next(names_iterator))
# print(next(names_iterator))
# print(next(names_iterator))
# print(next(names_iterator))
# print(next(names_iterator))
# print(next(names_iterator))

# print(next(iter(range(5))))

# print(round(1.9000990000000, 3))

# print(names)
# print(list(reversed(names)))
# print(names[::-1])

# print(names)
# print(list(sorted(names, reverse=True)))
# print(salaries)
# john = {"name": "John", "age": 23}
# marta = {"name": "Marta", "age": 30}
# james = {"name": "James", "age": 45}
# people = [john, marta, james]
# print(people)
# print(list(sorted(people, key=lambda man: man["age"], reverse=True)))
# print(type(str(True)))
# print(sum(salaries))
