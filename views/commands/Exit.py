

class Exit():
    def __init__(self, console_ui):
        self.descriptions = "Выход"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.exit()
