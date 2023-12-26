import pickle
from models import HumanModel

from models.FamilyModel.FamilyTree import FamilyTree


class FamilyTreeSerializer:
    @staticmethod
    def serialize(family_tree, filename: str):
        with open(filename, 'wb') as file:
            pickle.dump(family_tree, file)

    @staticmethod
    def deserialize(filename: str):
        with open(filename, 'rb') as file:
            family_tree = pickle.load(file)
        return family_tree


class FamilyTreeSort:
    @staticmethod
    def sort_family_tree(family_tree, key_func):
        sorted_items = sorted(family_tree.get_human_list(
        ).items(), key=lambda item: key_func(item[1].human))
        sorted_tree = dict(sorted_items)
        sorted_family_tree = FamilyTree()
        sorted_family_tree.set_human_list(sorted_tree)
        return sorted_family_tree

    @staticmethod
    def sort_by_first_name(family_tree):
        return FamilyTreeSort.sort_family_tree(family_tree, key_func=lambda human: human.first_name)

    @staticmethod
    def sort_by_last_name(family_tree):
        return FamilyTreeSort.sort_family_tree(family_tree, key_func=lambda human: human.last_name)

    @staticmethod
    def sort_by_age(family_tree):
        return FamilyTreeSort.sort_family_tree(family_tree, key_func=lambda human: human.age)


class Service():
    def __init__(self):
        self.family_tree = FamilyTree()

    def add_human(self, human: HumanModel):
        self.family_tree.add(human)

    def add_father(self, id_human: int, id_father: int):
        self.family_tree.add_father(id_human, id_father)

    def add_mother(self, id_human: int, id_mother: int):
        self.family_tree.add_mother(id_human, id_mother)

    def add_children(self, id_human: int, id_children: int):
        self.family_tree.add_children(id_human, id_children)

    def get_children(self, id_human: int):
        return self.family_tree.get_children(id_human)

    def get_father(self, id_human: int):
        return self.family_tree.get_father(id_human)

    def get_mother(self, id_human: int):
        return self.family_tree.get_mother(id_human)

    def save_to_file(self, file_name: str):
        FamilyTreeSerializer.serialize(self.family_tree, file_name)

    def load_to_file(self, file_name: str):
        self.family_tree = FamilyTreeSerializer.deserialize(file_name)

    def sort_by_age(self):
        self.family_tree = FamilyTreeSort.sort_by_age(self.family_tree)

    def sort_by_first_name(self):
        self.family_tree = FamilyTreeSort.sort_by_first_name(self.family_tree)

    def sort_by_last_name(self):
        self.family_tree = FamilyTreeSort.sort_by_last_name(self.family_tree)

    def print_all(self) -> str:
        return self.family_tree.__repr__()
