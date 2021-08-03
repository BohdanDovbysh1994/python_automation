class Company:
    def __init__(
        self,
        name,
        industry
    ):
        self.__name = name
        self.__industry = industry

    @property
    def name(self):
        return self.__name
