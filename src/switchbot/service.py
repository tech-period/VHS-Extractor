import json
import requests
import time

from asset import token as t
import commands

class service():
    def __init__(self):
        self.__body_base = "https://api.switch-bot.com/v1.0/devices"
        self.__header = {"Authorization" : t.token_id}
        self.__post_header = { 'Content-Type': 'application/json; charset: utf8', "Authorization" : t.token_id }
        self.__response = requests.get(self.__body_base, headers=self.__header)
        self.devices  = json.loads(self.__response.text)

        # Get "deviceId"
        self.bot_id  = [device["deviceId"] for device in self.devices['body']['infraredRemoteList'] if "レコーダー" == device['deviceName']]

        print(self.__response.text)

    def execute_command(self, command_name:str, wait_time:int = 0):
        cmd = commands.commands()
        url = self.__body_base + "/" + self.bot_id[0] + "/commands"
        # コマンドをAPIサーバーにPOSTして指定時間待機する
        requests.post(url, headers=self.__post_header, data=json.dumps(cmd.get_command(command_name)))
        time.sleep(wait_time)
        print("The \"" + command_name + "\" command was executed, and wait " + str(wait_time) + "second")

# 動作テスト
service = service()
service.execute_command("home", 3)
service.execute_command("up", 1)
service.execute_command("down", 1)
service.execute_command("enter", 1)