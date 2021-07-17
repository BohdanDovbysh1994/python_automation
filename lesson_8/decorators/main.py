# region example 1
# def star(func):
#     def inner(*args, **kwargs):
#         header, footer = "*" * 20, "*" * 20
#         return f"{header}\n{func(*args, **kwargs)}\n{footer}"
#     return inner
#
#
# def percent(func):
#     def inner(message: str):
#         header, footer = "%" * 20, "%" * 20
#         return f"{header}\n{func(message)}\n{footer}"
#     return inner

def add_footer_header(sign, quantity):
    """Dec doc"""
    def midleware_dec(func):
        """Middleware doc"""
        def inner(some):
            """Inner Doc"""
            footer = sign * quantity
            header = sign * quantity
            return f"{footer}\n{func(some)}\n{header}"
        return inner
    return midleware_dec


# @add_footer_header("*", 20)
@add_footer_header("$", 20)
def hi(msg):
    """Hi doc"""
    return msg


print(hi.__doc__)
# endregion
