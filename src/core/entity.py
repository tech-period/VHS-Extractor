import shelve

class entity():
    def __init__(self) -> None:
        self.entity = shelve.open('entity')
        if self.entity['data'] == None:
            self.entity['data'] = {
                'drive' : 'C:',
                'conditions': [
                    {'type':'8mm, miniDV','check':True,},
                    {'type':'VHS','check':False,}
                ]
            }
        print("前回条件")
        print(self.entity['data']['drive'])
        print(self.entity['data']['conditions'])
        # self.path = self.entity_data['path']
        # self.check_condition = self.entity_data['check_condition']
    
    def get(self, key:str, num:int = 0):
        result = str()
        if key == 'drive':
            result = self.entity['data'][key]
        elif key == 'type' or key == 'check':
            result = self.entity['data']['conditions'][num][key]
        else:
            print('not found entity field')
            result = None
        return result

    def set(self, key, data) -> None:
        locall_data = self.entity['data']
        locall_data[key] = data
        self.entity['data'] = locall_data

    def close(self) -> None:
        self.entity.close()