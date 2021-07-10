name_1 = "John"


def change_name():
    global name_1
    name_1 = "James"
    name_2 = "Marta"

    def dich():
        nonlocal name_2
        name_2 = "Bob"

    dich()
    print(name_2)


change_name()

print(name_1)
