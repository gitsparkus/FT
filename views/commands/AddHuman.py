

class AddHuman:
    def __init__(self, console_ui):
        self.descriptions = "Добавить человека"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.add_human()
