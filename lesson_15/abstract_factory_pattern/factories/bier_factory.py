from abc import ABC, abstractmethod


class BierFactory(ABC):
    _bier_type: str = ""

    @abstractmethod
    def get_bier(self, name: str):
        pass
