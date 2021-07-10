name = "John"  # Global scope
names = ["John", "Marta"]


def update_name():
    name = "James"  # local scope
    # names[1] = 1  # global variable modification since names mutable

    def internal():
        name = "Some"
        print(name)  # closing scope

    internal()


update_name()

print(name)
# print(names)
