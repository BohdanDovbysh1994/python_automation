# region example 1
def my_gen():
    counter = 0
    while counter < 100:
        yield counter ** 2
        counter += 1


generator = my_gen()


# for item in generator:
#     print(item)

some_list = list(range(100000))
numbers_iterator = iter(some_list)
next(numbers_iterator)
next(numbers_iterator)
next(numbers_iterator)
next(numbers_iterator)
next(generator)
next(generator)
next(generator)
next(generator)

import sys

print("LIST: ", sys.getsizeof(some_list))
print("ITERATOR: ", sys.getsizeof(numbers_iterator))
print("GENERATOR", sys.getsizeof(generator))



# # endregion

# region example 2
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n


# gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# endregion
