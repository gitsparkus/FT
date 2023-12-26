
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

    def print_answer(text: str):
        print(text)

    def start(self):
        self.__init__()
        while self.work:
            self.mainmenu.menu()
            self.execute()

    def add_human(self):
        print("Введите имя человека:")
        first_name = input()
        print("Введите фамилию человека:")
        last_name = input()
        print("Введите дату рождения (yyyy.mm.dd)")
        byear, bmonth, bday = list(map(int, input().split('.')))
        print(byear, bmonth, bday)
        print("Введите пол человека: F/M")
        gender = Gender.Male if input() == 'M'else Gender.Female
        print("Человек еще жив?: Y/N")
        if input() == "Y":
            self.presenter.add_human(
                Human(first_name, last_name, gender, datetime.date(byear, bmonth, bday), None))
        else:
            print("Введите дату рождения (yyyy.mm.dd)")
            dyear, dmonth, dday = list(map(int, input().split('.')))
            self.presenter.add_human(
                Human(first_name, last_name, gender, datetime.date(byear, bmonth, bday), datetime.date(dyear, dmonth, dday)))
        print(self.presenter.services.print_all())
        human = self.presenter.return_family_tree()
        print("23")

    def add_father(self):
        print("Введите ID ребенка: ")
        id_human = int(input())
        print("Введите ID отца: ")
        id_father = int(input())
        self.presenter.add_father(id_human, id_father)

    def add_mother(self):
        print("Введите ID ребенка: ")
        id_human = int(input())
        print("Введите ID матери: ")
        id_mother = int(input())
        self.presenter.add_mother(id_human, id_mother)

    def print_all_human(self):
        print(self.presenter.print_all_human())

    def execute(self):
        print("Введите номер команды:")
        command = int(input())
        self.mainmenu.execute(command)

    def print_all_human(self):
        prnt = self.presenter.print_all_human()
        if print:
            print(prnt)

    def save_to_file(self):
        print("Напишите имя файла для сохранения:")
        self.presenter.save_to_file(input())

    def load_to_file(self):
        print("Напишите имя файла для загрузки:")
        self.presenter.load_to_file(input())

    def add_children(self):
        print("Введите ID человека:")
        id_human = int(input())
        print("Введите ID ребенка:")
        id_children = int(input())
        self.presenter.add_children(id_human, id_children)

    def sort_by_age(self):
        self.presenter.sort_by_age()
        print("Отсортированное семейное дерево:")
        self.print_all_human()

    def sort_by_first_name(self):
        self.presenter.sort_by_first_name()
        print("Отсортированное семейное дерево:")
        self.presenter.print_all_human()

    def sort_by_last_name(self):
        self.presenter.sort_by_last_name()
        print("Отсортированное семейное дерево:")
        self.presenter.print_all_human()

    def exit(self):
        print("Завершение работы.")
        self.work = False
