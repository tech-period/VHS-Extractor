import shelve

class entity():
    def __init__(self) -> None:
        self.entity = shelve.open('entity')
        # self.entity['data'] = {'drive' : 'C:', 'path': '%USERPROFILE%'}
        print("前回条件")
        print(self.entity['data']['drive'])
        print(self.entity['data']['path'])
        # self.path = self.entity_data['path']
        # self.check_condition = self.entity_data['check_condition']
    
    def get(self, key):
        return self.entity['data'][key]

    def set(self, key, data) -> None:
        locall_data = self.entity['data']
        locall_data[key] = data
        self.entity['data'] = locall_data

    def close(self) -> None:
        self.entity.close()