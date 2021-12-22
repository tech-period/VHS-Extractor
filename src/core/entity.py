import shelve

class entity():
    def __init__(self) -> None:
        self.entity = shelve.open('entity')
        # if True:
        if self.entity['data'] == None:
            self.entity['data'] = {
                'drive' : 'C:',
                'conditions': [
                    {'type':'8mm, miniDV','check':True,},
                    {'type':'VHS','check':False,}
                ]
            }
    
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

    def set(self, key, data, num:int = 0) -> None:
        locall_data = self.entity['data']
        if key == 'drive':
            locall_data[key] = data
        elif key == 'type' or key == 'check':
            locall_data['conditions'][num][key] = data
        else:
            print('not found entity field')
        self.entity['data'] = locall_data

    def close(self) -> None:
        self.entity.close()