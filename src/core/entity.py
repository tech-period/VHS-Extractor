import shelve

class entity():
    def __init__(self) -> None:
        self.entity = shelve.open('entity')
        # if True:
        try:
            self.entity['data']
        except:
            self.entity['data'] = {
                'drive' : 'C:',
                'conditions': [
                    {'type':'8mm, miniDV', 'time':0, 'check':True,},
                    {'type':'VHS', 'time':0, 'check':False,}
                ]
            }
    
    def get(self, key:str, num:int = 0):
        result = str()
        if key == 'drive':
            result = self.entity['data'][key]
        elif key == 'type' or key == 'time' or key == 'check':
            result = self.entity['data']['conditions'][num][key]
        else:
            print('not found entity field')
            result = None
        return result

    def set(self, key, data, num:int = 0) -> None:
        locall_data = self.entity['data']
        if key == 'drive':
            locall_data[key] = data
        elif key == 'type' or key == 'time' or key == 'check':
            locall_data['conditions'][num][key] = data
        else:
            print('not found entity field')
        self.entity['data'] = locall_data

    def close(self) -> None:
        self.entity.close()