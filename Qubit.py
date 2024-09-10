from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

class Qubit(metaclass=ABCMeta):
    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def measure(self) -> bool:
        pass

    @abstractmethod
    def reset(self):
        pass