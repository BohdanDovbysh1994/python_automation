from lesson_15.adapter_pattern.csv_to_json_adapter import CSVToJsonAdapter

with open("users.csv") as file:
    lines = file.readlines()

names = lines[0]
data = lines[1:]

adapter = CSVToJsonAdapter(names, data)
print(adapter.get_json())
