import time
from threading import Lock, RLock, Semaphore


class Employee:
    def __init__(self):
        self.rate = 0
        self.__lock = Semaphore(1)

    def increase_rate(self):
        self.__lock.acquire()

        local_value = self.rate
        local_value += 10
        time.sleep(0.1)
        self.rate = local_value

        self.__lock.release()
