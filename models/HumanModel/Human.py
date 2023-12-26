
from models.HumanModel.EntityInterface import EntityInterface
from datetime import datetime, date, time, timedelta
from .GenderModel import Gender
from dateutil.relativedelta import relativedelta


class Human(EntityInterface):

    def __init__(self, first_name: str, last_name: str, gender: Gender, birth_date: date, death_date: date):
        self._id = -1
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._birth_date = birth_date
        self._death_date = death_date
        self._age = self.calculate_age()

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def set_id(self, id: int):
        self._id = id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def set_first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def set_last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def death_date(self):
        return self._death_date

    @death_date.setter
    def set_death_date(self, death_date: date):
        self._death_date = death_date
        self.calculate_age()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def set_birth_date(self, birth_date: date):
        self._birth_date = birth_date
        self.calculate_age()

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def set_gender(self, gender: Gender):
        self._gender = gender

    def calculate_age(self):
        if self._death_date is None:
            self._age = relativedelta(datetime.now(), self._birth_date).years
            return self._age
        else:
            self._age = relativedelta(self._death_date, self._birth_date).years
            return self._age

    def get_age(self):
        return self._age

    def __repr__(self) -> str:
        return f"ID: {self._id} Имя: {self._first_name} Фамилия: {self._last_name} Пол: {self._gender} Возраст: {self.get_age()}"

    def __str__(self) -> str:
        return self.__repr__()
