class FamilyTree:
    def __init__(self):
        self.roots = []

    def add_person(self, person):
        if person not in self.roots:
            self.roots.append(person)
    
    def as_dict(self):
        return {
            'roots': [root.as_dict() for root in self.roots]
        }