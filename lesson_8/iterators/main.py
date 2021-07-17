numbers = [1, 2, 3, 4, 5]  # simple list - sequence
numbers_iterator = iter(numbers)  # iterator of numbers

# print(numbers_iterator)

for number in numbers_iterator:  # one of possible ways for iterating iterator
    print(number)

while True:
    print(next(numbers_iterator))
