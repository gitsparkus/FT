from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def print_answer(text: str):
        pass

    @abstractmethod
    def start():
        pass
