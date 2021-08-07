class Phone:
    def __init__(self):
        self.__model = "IPhone"
        self.__system = "IOS"
        self.__space = "1GB"

    def __call__(self, number: str):
        print(f"I am calling {number} number...")


if __name__ == '__main__':
    phone = Phone()
    phone("+380502654556")
