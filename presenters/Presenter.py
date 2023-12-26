
from services.Services import Service


class Presenter():
    def __init__(self):
        self.services = Service()

    def add_human(self, human):
        self.services.add_human(human)

    def add_father(self, id_human: int, id_father: int):
        self.services.add_father(id_human, id_father)

    def add_mother(self, id_human: int, id_mother: int):
        self.services.add_mother(id_human, id_mother)

    def print_all_human(self):
        return self.services.print_all()

    def save_to_file(self, file_name: str):
        self.services.save_to_file(file_name)

    def load_to_file(self, file_name: str):
        self.services.load_to_file(file_name)

    def return_family_tree(self):
        return self.services.family_tree

    def add_children(self, id_human, id_children):
        self.services.add_children(id_human, id_children)

    def sort_by_age(self):
        self.services.sort_by_age()

    def sort_by_first_name(self):
        self.services.sort_by_first_name()

    def sort_by_last_name(self):
        self.services.sort_by_last_name()
