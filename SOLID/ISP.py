from abc import ABC, abstractmethod


class IInvincible(ABC):
    @abstractmethod
    def win(self):
        pass

