from lesson_15.proxy_pattern.proxy_csv_manager import ProxyCsvManager
from lesson_15.proxy_pattern.csv_manager import CsvManager


csv_reader = CsvManager("users.csv")
reader = ProxyCsvManager(csv_reader)

print(reader.read())
print(reader.read())
reader.write("\nAmanda,Stuart,56,Female,700")
print(reader.read())
