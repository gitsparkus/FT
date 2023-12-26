from collections import namedtuple
from models import HumanModel

PersonInfo = namedtuple('PersonInfo', ['human', 'father', 'mother'])


class FamilyTree():
    def __init__(self):
        self._id = -1
        self._human_list = dict()

    def get_human_list(self):
        return self._human_list

    def set_human_list(self, human_list):
        self._human_list = human_list

    def get_human(self, id_human: int):
        if self._human_list.get(id_human, None):
            return self._human_list[id_human]

    def add(self, human: HumanModel):
        self._id += 1
        human.set_id = self._id
        self._human_list.setdefault(self._id, PersonInfo(human, None, None))

    def add_father(self, id_human: int, id_father: int):
        if self._human_list.get(id_human) and self._human_list.get(id_father):
            person_info = self._human_list[id_human]
            father_info = self._human_list[id_father]
            new_person_info = PersonInfo(
                person_info.human, father_info.human, person_info.mother)
            self._human_list[id_human] = new_person_info

    def add_mother(self, id_human: int, id_mother: int):
        if self._human_list.get(id_human) and self._human_list.get(id_mother):
            person_info = self._human_list[id_human]
            mother_info = self._human_list[id_mother]
            new_person_info = PersonInfo(
                person_info.human, person_info.father, mother_info.human)
            self._human_list[id_human] = new_person_info

    def add_children(self, id_human, id_children):
        if self._human_list.get(id_human) and self._human_list.get(id_children):
            parent_gender = self._human_list[id_human].gender
            existing_father = self._human_list[id_children].father
            existing_mother = self._human_list[id_children].mother

            if parent_gender == GenderModel.Gender.Male:
                if existing_father is None and existing_mother is None:
                    self.add_father(id_children, id_human)
            else:
                if existing_father is None and existing_mother is None:
                    self.add_mother(id_children, id_human)

    def get_father(self, id_human: int):
        person_info = self._human_list.get(id_human)
        if person_info:
            return person_info.father

    def get_mother(self, id_human: int):
        person_info = self._human_list.get(id_human)
        if person_info:
            return person_info.mother

    def get_children(self, id_human: int):
        children = []
        for person_id, person_info in self._human_list.items():
            father_id = person_info.father.id if person_info.father else None
            mother_id = person_info.mother.id if person_info.mother else None

            if father_id == id_human or mother_id == id_human:
                children.append(person_info.human)

        return children

    def get_human_list(self):
        return self._human_list

    def __getitem__(self, index):
        return self._human_list.get(index, None)

    def __repr__(self) -> str:
        return "".join([f'{v[0]} \n Отец: {v[1]} \n Мать: {v[2]} \n Дети: {[f"{h}" for h in self.get_children(v[0]._id)]} \n' for k, v in self._human_list.items()])

    def __str__(self) -> str:
        return self.__repr__()
