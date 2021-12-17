from _typeshed import Self
import shelve

class entity():
    def __init__(self) -> None:
        self.entity_data = shelve.open('entity')
        self.drive = self.entity_data['drive']
        self.path = self.entity_data['path']
        self.check_condition = self.entity_data['check_condition']
    
    def get(self, key):
        return self.entity_data[key]

    def set(self, key, data) -> None:
        self.entity_data[key] = data