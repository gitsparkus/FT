
from views.commands.AddChildren import AddChildren
from views.commands.AddFather import AddFather
from views.commands.AddHuman import AddHuman
from views.commands.AddMother import AddMother
from views.commands.Exit import Exit
from views.commands.LoadFile import LoadFile
from views.commands.PrintAll import PrintAll
from views.commands.SaveFile import SaveFile
from views.commands.SortByAge import SortByAge
from views.commands.SortByFirstName import SortByFirstName
from views.commands.SortByLastName import SortByLastName


class MainMenu():
    def __init__(self, console_ui):
        self.command_list = []
        self.command_list.append(AddHuman(console_ui))
        self.command_list.append(AddFather(console_ui))
        self.command_list.append(AddMother(console_ui))
        self.command_list.append(AddChildren(console_ui))
        self.command_list.append(SortByAge(console_ui))
        self.command_list.append(SortByFirstName(console_ui))
        self.command_list.append(SortByLastName(console_ui))
        self.command_list.append(PrintAll(console_ui))
        self.command_list.append(SaveFile(console_ui))
        self.command_list.append(LoadFile(console_ui))
        self.command_list.append(Exit(console_ui))

    def menu(self):
        [print(f"{x}. {self.command_list[x].descriptions}")
         for x in range(len(self.command_list))]

    def execute(self, number: int):
        commands = self.command_list[number].execute()
