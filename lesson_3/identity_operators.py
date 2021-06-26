names_1 = [1, 2, 3, 4]
names_2 = names_1.copy()

print(id(names_1))
print(id(names_2))

print(names_1 == names_2)
print(names_1 is names_2)
print(names_1 is not names_2)