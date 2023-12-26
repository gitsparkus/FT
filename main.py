
import datetime
from models.FamilyModel.FamilyTree import FamilyTree
from models.HumanModel import Human
from models.HumanModel.EntityInterface import EntityInterface
from models.HumanModel.GenderModel import Gender
from models.HumanModel.Human import Human
from services.Services import FamilyTreeSerializer, FamilyTreeSort, Service
from views.ConsoleUI import ConsoleUI

tom = Human("Tom", "Smith", Gender.Male, datetime.date(
    1990, 10, 12), datetime.date(2023, 10, 12))

cat = Human("Cat", "Smith", Gender.Male, datetime.date(
    1980, 10, 12), None)

bill = Human("Bill", "Smith", Gender.Male, datetime.date(
    1970, 10, 12), None)

# f = FamilyTree()
# f.add(tom)
# f.add(cat)
# f.add(bill)
# f.add_father(0, 2)
# f.add_mother(0, 1)
# # print(f.get_children(1))
# FamilyTreeSerializer.serialize(f, 'test.pkl')
# f = FamilyTreeSerializer.deserialize('test.pkl')
# print(f)
# f = FamilyTreeSort.sort_by_first_name(f)
# print(f)
# serv = Service()
# serv.add_human(tom)
# cui = ConsoleUI()
# cui.add_human()
ui = ConsoleUI()
ui.start()
