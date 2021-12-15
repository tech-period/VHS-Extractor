import os

class service():
    def __init__(self) -> None:
        pass

    def get_drives(self):
        return [ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
