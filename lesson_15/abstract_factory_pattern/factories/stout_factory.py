from lesson_15.abstract_factory_pattern.factories.bier_factory import \
    BierFactory


class StoutFactory(BierFactory):
    _bier_type = "Stout"

    def __init__(self):
        self.__name = "Rogan"
        self.__positions = ["Imperial", "Milk", "Dry"]

    @property
    def positions(self):
        return self.__positions

    def get_bier(self, name: str):
        if name == "Milk":
            return "Your milk stout"
