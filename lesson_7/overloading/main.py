import multipledispatch
from multipledispatch import dispatch


@dispatch(str)
def get_wallet(user_id: str) -> str:
    """
        Returns wallet by user id
    """
    return user_id


@dispatch(str, str)
def get_wallet(user_id: str, deposit_id: str) -> str:
    """
        Returns wallet by user id and deposit id
    """
    return user_id + deposit_id


if __name__ == '__main__':

   get_wallet("test")
