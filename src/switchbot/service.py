import json
import requests
import time

from asset import token as t
import commands

class service():
    def __init__(self):
        self.body_base = "https://api.switch-bot.com/v1.0/devices"
        self.header = {"Authorization" : t.token_id}
        self.post_header = { 'Content-Type': 'application/json; charset: utf8', "Authorization" : t.token_id }
        self.response = requests.get(self.body_base, headers=self.header)        
        self.devices  = json.loads(self.response.text)

        # Get switchbot bot "deviceId" in all device information
        # self.bots_id  = [device["deviceId"] for device in self.devices['body']['deviceList']]
        self.bots_id  = [device["deviceId"] for device in self.devices['body']['infraredRemoteList']]

        print(self.response.text)



this = service()
cmd = commands.commands()

url = this.body_base + "/" + this.bots_id[0] + "/commands"
print("url : " + url)

print("body_home")
result = requests.post(url, headers=this.post_header, data=json.dumps(cmd.home))
time.sleep(3)

print("body_up")
result = requests.post(url, headers=this.post_header, data=json.dumps(cmd.up))
time.sleep(1)

print("body_down")
result = requests.post(url, headers=this.post_header, data=json.dumps(cmd.down))
time.sleep(1)

print("body_enter")
result = requests.post(url, headers=this.post_header, data=json.dumps(cmd.enter))
time.sleep(1)
