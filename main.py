from Person import Person
from FamilyTree import FamilyTree
from WriteAndRead import WriteAndRead
from UI import Ui

tree = FamilyTree()
war = WriteAndRead()

Ivan = Person('Ivan', 1740)
tree.add_person(Ivan)
Anna = Person('Anna', 1840)
tree.add_person(Anna)
Person.add_child(Ivan, Anna)
war.save_to_file('family_tree.json', tree)
tree = war.load_from_file('family_tree.json')

Ui.command_msg(tree)

