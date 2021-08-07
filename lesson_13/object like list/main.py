class Building:
    def __init__(self):
        self.__stages = [None]

    def __setitem__(self, key, value):
        try:
            self.__stages[key] = value
        except IndexError as e:
            result = [None] * (len(self.__stages) * 2)
            for index, item in enumerate(self.__stages):
                result[index] = item
            self.__stages = result
            self.__stages[key] = value

    def __getitem__(self, item):
        return self.__stages[item]

    def __str__(self):
        return f"{self.__stages}"

if __name__ == '__main__':
    building = Building()
    building[0] = "Toyora"
    building[1] = "Global Logic"
    building[2] = "BMW"
    print(building[1])
    print(building)