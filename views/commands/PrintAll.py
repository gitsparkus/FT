

class PrintAll():
    def __init__(self, console_ui):
        self.descriptions = "Напечатать всех"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.print_all_human()
