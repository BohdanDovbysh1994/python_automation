# some_list = [1, 2, 3, 4, 5]

# list comprehension
# print([item for item in some_list if item > 3])

# list comprehension generation of list
# new_list = [item ** 2 for item in range(100)]
# print(new_list)

# NEVER DO THAT!!!
# print([print(item) for item in range(100)])

# names = ["John", "Marta", "James"]

# print(next(enumerate(names)))
# new_dict = {index: name for index, name in enumerate(names) if name.startswith("J")}
# print(new_dict)

# new_set = {item for item in [1, 1, 2, 3, 4, 5, 5, 6, 6, 66] if item > 4}
# print(new_set)

# generate tuples with comprehensions
import sys
new_list = [item for item in range(10000)]

# new_gen = (*(item for item in range(100)), )
# print(sys.getsizeof(new_list))
# print(sys.getsizeof(new_gen))
# for item in new_gen:
#     print(item)
# print(new_gen)
# print((1, 2, 3))
# new_tuple = 1,
# print(new_tuple)
