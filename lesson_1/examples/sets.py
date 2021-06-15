not_unique_names = ["John", "Marta", "John", "Brandon"]

unique_names_1 = {*not_unique_names}
unique_names_2 = set(not_unique_names)

print(unique_names_1)
print(unique_names_2)

unique_names_1.add("Barak")
print(unique_names_1)