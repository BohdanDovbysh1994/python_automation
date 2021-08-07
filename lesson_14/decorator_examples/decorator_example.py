from typing import Callable


# class Power:
#     def __init__(self, function):
#         self.__function = function
#
#     def __call__(self, a, b):
#         return self.__function(a, b) ** 2
#
#
# def multiply_together(a, b):
#     return a * b


# -----------------------------------------------------
class Power:
    def __init__(self, pow: int):
        self.__pow = pow

    def __call__(self, function):
        def inner(a, b):
            return function(a, b) ** self.__pow
        return inner


# @Power(2)
# def multiply_together(a, b):
#     return a * b


# if __name__ == '__main__':
#     print(multiply_together(2, 2))
