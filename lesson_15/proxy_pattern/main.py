from lesson_15.proxy_pattern.csv_proxy_reader import CsvProxyReaderWriter
from lesson_15.proxy_pattern.csv_reader import CsvReaderWriter

csv_reader = CsvReaderWriter("users.csv")
reader = CsvProxyReaderWriter(csv_reader)

print(reader.read())
print(reader.read())
reader.write("Amanda,Stuart,56,Female,700")
print(reader.read())
