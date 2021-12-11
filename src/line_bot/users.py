class users():
    def __init__(self) -> None:
        self.__users = {
            "name" : "id",
        }
    
    # Single getter
    def get_use(self,name:str) -> str:
        user = self.__users[name]
        return user

    # All getter
    def get_users(self):
        return self.__users.values
        