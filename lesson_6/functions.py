numbers = [1, 2, 3, 4, 5]
names = ["John", "Anton", "Marta", "Jura"]


def iterate_sequence(sequence: list):
    for element in sequence:
        print(element)


if __name__ == '__main__':
    iterate_sequence(numbers)
    iterate_sequence(names)
