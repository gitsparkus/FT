

class AddChildren():
    def __init__(self, console_ui):
        self.descriptions = "Добавить ребенка"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.add_children()
