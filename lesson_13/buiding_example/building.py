class Building:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address
        self.__stages = dict()

    def __len__(self):
        return len(self.__stages)

    def __setitem__(self, key, value):
        self.__stages[key] = value

    def __getitem__(self, item: int):
        return self.__stages[item]
