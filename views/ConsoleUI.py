from models.HumanModel.GenderModel import Gender

from presenters.Presenter import Presenter
from views.MainMenu import MainMenu
from views.ViewInterface import View
from models.HumanModel.Human import Human

import datetime


class ConsoleUI(View):

    def __init__(self):
        self.presenter = Presenter()
        self.work = True
        self.mainmenu = MainMenu(self)

    @staticmethod
    def print_answer(text: str):
        print(text)

    def start(self):
        self.__init__()
        while self.work:
            self.mainmenu.menu()
            self.execute()

    def add_human(self):
        first_name = input('Введите имя человека: ')
        last_name = input('Введите фамилию человека: ')
        byear, bmonth, bday = list(map(int, input('Введите дату рождения (yyyy.mm.dd) ').split('.')))

        gender = Gender.Male if input('Введите пол человека: F/M ') == 'M' else Gender.Female

        if input('Человек еще жив?: Y/N ') == 'Y':
            self.presenter.add_human(
                Human(first_name, last_name, gender, datetime.date(byear, bmonth, bday), None))
        else:
            dyear, dmonth, dday = list(map(int, input('Введите дату рождения (yyyy.mm.dd) ').split('.')))
            self.presenter.add_human(
                Human(first_name, last_name, gender, datetime.date(byear, bmonth, bday),
                      datetime.date(dyear, dmonth, dday)))
        print(self.presenter.services.print_all())
        human = self.presenter.return_family_tree()

    def add_father(self):
        id_human = int(input('Введите ID ребенка: '))
        id_father = int(input('Введите ID отца: '))
        self.presenter.add_father(id_human, id_father)

    def add_mother(self):
        id_human = int(input('Введите ID ребенка: '))
        id_mother = int(input('Введите ID матери: '))
        self.presenter.add_mother(id_human, id_mother)

    def print_all_human(self):
        print(self.presenter.print_all_human())

    def execute(self):
        command = int(input('Введите номер команды: '))
        self.mainmenu.execute(command)

    def print_all_human(self):
        if to_print := self.presenter.print_all_human():
            print(to_print)
        else:
            print('Нет данных')

    def save_to_file(self):
        self.presenter.save_to_file(input('Напишите имя файла для сохранения: '))

    def load_to_file(self):
        self.presenter.load_to_file(input('Напишите имя файла для загрузки: '))

    def add_children(self):
        id_human = int(input('Введите ID человека: '))
        id_children = int(input('Введите ID ребенка: '))
        self.presenter.add_children(id_human, id_children)

    def sort_by_age(self):
        self.presenter.sort_by_age()

    def sort_by_first_name(self):
        self.presenter.sort_by_first_name()

    def sort_by_last_name(self):
        self.presenter.sort_by_last_name()

    def exit(self):
        print('Завершение работы.')
        self.work = False
