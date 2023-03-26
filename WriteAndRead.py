import json
from Person import Person
from FamilyTree import FamilyTree

class WriteAndRead:
    def save_to_file(self, filename, tree):
        with open(filename, 'w') as file:
            json.dump(tree.as_dict(), file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            tree = FamilyTree()
            for root in data['roots']:
                perec = self.load_person(root)
                tree.add_person(perec)
            return tree

    def load_person(self, data):
        name = data['name']
        birth_year = data['birth_year']
        person = Person(name, birth_year)
        for child in data['children']:
            little_perec = self.load_person(child)
            person.add_child(little_perec)
        return person 