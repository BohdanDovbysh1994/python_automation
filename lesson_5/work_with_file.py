# # with open("text.txt") as file:
# #     lines = file.readlines()
#
# # file = open("text.txt", "r")
# # print(file.readlines())
# # file.close()
#
# # for line in lines:
# #     login, password = line.split(' ')
# #     print(f"Login: {login}\nPassword: {password}")
#
# # login(login, password)
#
# import pickle
#
# numbers = [1, 2, 3, 4, 5]
# str_numbers = []
#
# with open("text.txt", "r+b") as file:
#     text = pickle.dumps(numbers)
#     file.write(text)
#
#     byte_text = file.read()
#     print(byte_text)
#     numbers_2 = pickle.loads(byte_text)
#
# print(numbers_2)
