from linebot import LineBotApi
from linebot.models import TextSendMessage

from .asset.token import token
from .users import users

class service():
    def __init__(self) -> None:
        self.__LINE_ACCESS_TOKEN = token
        self.line_bot = LineBotApi(self.__LINE_ACCESS_TOKEN)
        self.users = users()

    def push_message(self, message:str):
        text_send_message = TextSendMessage(text=message)
        users = self.users.get_users()
        print("push message to some accounts with [" + message + "]")
        for user_id in users:
            self.line_bot.push_message(user_id, messages=text_send_message)
