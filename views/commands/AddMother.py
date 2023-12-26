

class AddMother():
    def __init__(self, console_ui):
        self.descriptions = "Добавить мать"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.add_mother()
