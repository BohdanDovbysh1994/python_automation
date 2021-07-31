from abc import ABC, abstractmethod


class IFlyable(ABC):
    @abstractmethod
    def fly(self):
        """Declare fly behaviour for child classes"""
        pass

    @abstractmethod
    def nosedive(self):
        """Declare nosedive behaviour for child classes"""
        pass

    @abstractmethod
    def take_off(self):
        pass

    @abstractmethod
    def land(self):
        pass
