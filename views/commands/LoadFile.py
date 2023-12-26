

class LoadFile():
    def __init__(self, console_ui):
        self.descriptions = "Загрузить из файла"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.load_to_file()
