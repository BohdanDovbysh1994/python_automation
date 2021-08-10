from lesson_15.abstract_factory_pattern.factories.bier_factory import \
    BierFactory


class LagerFactory(BierFactory):
    _bier_type = "Lager"

    def __init__(self):
        self.__name = "Obolon"
        self.__positions = ["Light", "Super Light"]

    @property
    def positions(self):
        return self.__positions
