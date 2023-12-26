

class SaveFile():
    def __init__(self, console_ui):
        self.descriptions = "Сохранить в файл"
        self.console_ui = console_ui

    def execute(self):
        self.console_ui.save_to_file()
