from abc import ABC, abstractmethod, abstractproperty
from datetime import date

from .GenderModel import Gender


class EntityInterface(ABC):

    @abstractproperty
    def id(self):
        pass

    @id.setter
    @abstractmethod
    def set_id(self, id: int):
        pass

    @abstractproperty
    def first_name(self):
        pass

    @first_name.setter
    @abstractmethod
    def set_first_name(self, first_name: str):
        pass

    @abstractproperty
    def last_name(self):
        pass

    @last_name.setter
    @abstractmethod
    def set_last_name(self, last_name: str):
        pass

    @abstractproperty
    def death_date(self) -> date:
        pass

    @death_date.setter
    @abstractmethod
    def set_death_date(self, death_date: date):
        pass

    @abstractproperty
    def birth_date(self) -> date:
        pass

    @birth_date.setter
    @abstractmethod
    def set_birth_date(self, birth_date: date):
        pass

    @abstractproperty
    def gender(self) -> Gender:
        pass

    @abstractmethod
    def set_gender(self, gender: Gender):
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
