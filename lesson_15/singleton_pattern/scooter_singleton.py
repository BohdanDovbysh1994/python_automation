from typing import Type


def singleton(_class: Type):
    def inner(*args):
        if not hasattr(_class, "instance"):
            setattr(_class, "instance", _class(*args))
        return getattr(_class, "instance")
    return inner
