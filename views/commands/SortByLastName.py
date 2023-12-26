

class SortByLastName():
    def __init__(self, console_ui):
        self.descriptions = "Отсортировать по фамилии"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.sort_by_last_name()
