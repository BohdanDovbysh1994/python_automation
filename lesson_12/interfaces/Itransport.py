from abc import ABC, abstractmethod


class ITransport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def move(self, direction: str, distance: int):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
