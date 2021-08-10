from lesson_15.abstract_factory_pattern.factories.bier_factory import \
    BierFactory
from lesson_15.abstract_factory_pattern.factories.lagger_factory import \
    LagerFactory
from lesson_15.abstract_factory_pattern.factories.stout_factory import \
    StoutFactory


class AbstractFactory:
    @staticmethod
    def get_factory(bier_type: str) -> BierFactory:
        if bier_type == "Staut":
            return StoutFactory()
        elif bier_type == "Lager":
            return LagerFactory()
        else:
            raise Exception("Incorrect name of bier(")


if __name__ == '__main__':
    factory = AbstractFactory.get_factory("Lager")
    print(factory.get_bier("Milk"))
