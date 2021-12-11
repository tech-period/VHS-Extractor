from linebot import LineBotApi
from linebot.models import TextSendMessage

from .asset.token import token
from .users import users

class service():
    def __init__(self) -> None:
        self.__LINE_ACCESS_TOKEN = token
        self.line_bot = LineBotApi(self.__LINE_ACCESS_TOKEN)

    def push_message(self, message:str):
        user_id = users.get_user("Genki")
        message = TextSendMessage(text="指定の処理が完了しました")
        self.line_bot.push_message(user_id, messages=message)
