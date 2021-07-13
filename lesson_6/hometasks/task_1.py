from unittest import TestCase

from typing import Union


def arithmetic(
    left_operand: Union[int, float],
    right_operand: Union[int, float],
    /,
    *,
    operation: str
) -> Union[int, float, str]:
    """
        Apply arithmetic operation for provided left and right operands
    """
    if operation == '+':
        return left_operand + right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    else:
        return f"Not known operation: {operation}"


if __name__ == "__main__":
    # assert arithmetic(3, 4, operation="*") == 12
    # assert arithmetic(3, 4, operation="+") == 7
    # assert arithmetic(25, 5, operation="/") == 5
    # assert type(arithmetic(25, 5, operation="/")) == float
    # assert arithmetic(5, 5, operation="//") == f"Not known operation: //"
    # assert arithmetic.__doc__ == (
    #     f"\n{' ' * 8}"
    #     f"Apply arithmetic operation for provided left and right operands\n"
    #     f"{' ' * 4}"""
    # )
    # assert arithmetic.__code__.co_name == "arithmetic"
    # assert arithmetic.__code__.co_varnames == ("left_operand", "right_operand", "operation")
    # try:
    #     arithmetic(1, 2, 3)
    # except TypeError as e:
    #     assert e.__class__ is TypeError
    # try:
    #     arithmetic(left_operand=1, right_operand=2, operation="+")
    # except TypeError as e:
    #     assert e.__class__ is TypeError
    #
    # try:
    #     arithmetic(1, right_operand=2, operation="+")
    # except TypeError as e:
    #     assert e.__class__ is TypeError

    class Task1Test(TestCase):
        def test_check_result_of_multipy(self):
            assert arithmetic(3, 4, operation="*") == 12

        def test_check_result_of_sum(self):
            assert arithmetic(3, 4, operation="+") == 7

        def test_check_result_of_divide(self):
            assert arithmetic(25, 5, operation="/") == 5

        def test_check_type_of_value_after_divide(self):
            assert type(arithmetic(25, 5, operation="/")) == float

        def test_check_message_for_default(self):
            assert arithmetic(5, 5, operation="//") == f"Not known operation: //"

        def test_check_docstring(self):
            assert arithmetic.__doc__ == (
                f"\n{' ' * 8}"
                f"Apply arithmetic operation for provided left and right operands\n"
                f"{' ' * 4}"""
            )

        def test_check_name_of_function(self):
            assert arithmetic.__code__.co_name == "arithmetic"

        def test_check_argument_names(self):
            assert arithmetic.__code__.co_varnames == ("left_operand", "right_operand", "operation")

        def test_check_type_error_if_operator_is_positionsl(self):
            try:
                arithmetic(1, 2, 3)
            except TypeError as e:
                assert e.__class__ is TypeError

        def test_check_type_error_if_left_and_right_operands_keyword(self):
            try:
                arithmetic(left_operand=1, right_operand=2, operation="+")
            except TypeError as e:
                assert e.__class__ is TypeError

        def test_check_type_error_if_right_operand_keyword(self):
            try:
                arithmetic(1, right_operand=2, operation="+")
            except TypeError as e:
                assert e.__class__ is TypeError
