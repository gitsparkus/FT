from abc import ABC, abstractmethod


class View(ABC):

    @staticmethod
    @abstractmethod
    def print_answer(text: str):
        pass

    @abstractmethod
    def start(self):
        pass
