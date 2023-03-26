class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.children = []       

    def add_child(self, child):
        self.children.append(child)

    def as_dict(self):
        return {
            'name': self.name, 
            'birth_year': self.birth_year,
            'children': [child.as_dict() for child in self.children]
        }
