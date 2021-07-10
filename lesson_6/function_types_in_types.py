from typing import List


# def get_wallet(user_id: str, deposits: List[str]):
#     for deposit in deposits:
#         print(deposit)
#     user_id.split(" ")
#
#
# get_wallet(deposits=["some", "some 2"], user_id="some some")

# def print_names(*arg):
#     print(*arg)
#
# print_names("John", "James", "Marta")


# def get_wallet(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# john = {"name": "John", "age": 23}
#
#
# get_wallet(**john)

# def some(*args):
#     print(*args)
#
# names = ["John", "Marta"]
# some(1, 2, 3, 4, 5)
# some(*names)

# def some(name: str, age: int = 23):
#     print(name, age)
#
#
# some("john")
# some("marta", 34)


# def get_wallets(deposits: List[str] = ["some"]):
#     deposits.append("text")
#     print(deposits)
#
#
# get_wallets()
# get_wallets()
# get_wallets()
# get_wallets()
# get_wallets()
# get_wallets()
# get_wallets()




def some(*, name, age, gender):
    pass

john = {"first_name": "john", "last_name": "Dow", "age": 23, "gender": "male"}
# some("john", age=23, gender="male")  # Error
some(**john)  # Error
