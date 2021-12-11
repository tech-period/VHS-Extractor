from linebot import LineBotApi
from linebot.models import TextSendMessage

from .asset.token import token
from .users import users

class service():
    def __init__(self) -> None:
        self.__LINE_ACCESS_TOKEN = token
        self.line_bot = LineBotApi(self.__LINE_ACCESS_TOKEN)
        self.users = users()
        print("インスタンス化完了")

    def push_message(self, message:str):
        print("def")
        message = TextSendMessage(text=message)

        genki_id = self.users.get_user("genki")
        self.line_bot.push_message(genki_id, messages=message)
        
        sachika_id = self.users.get_user("sachika")
        self.line_bot.push_message(sachika_id, messages=message)
