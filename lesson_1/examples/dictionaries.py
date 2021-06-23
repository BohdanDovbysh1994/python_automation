john = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 25,
    "gender": "male",
    "parents": ["John Smith Junio", "Marta Smith"]
}

print(john)


for key, value in john.items():
    # print(key, value, sep=" => ")
    print(f"{key} => {value}")


marta = {
    "first_name": "Marta",
    "last_name": "Dow",
    "age": 25,
    "gender": "male",
    "parents": []
}


john = {
    "first_name": "John",
    "last_name": "Dow",
    "age": 25,
    "gender": "male",
    "parents": [marta]
}
