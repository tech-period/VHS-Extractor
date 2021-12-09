import json
import requests
import time

from asset import token as t

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

# Get all switchbot bot power state and output on your display
for bot_id in this.bots_id:
 
    # create API body 
    # suport cool state 
    body_home = {
        "command": "ホーム",
        "parameter": "default",
        "commandType": "customzie"
    }
    body_left = {
        "command": "左",
        "parameter": "default",
        "commandType": "customzie"
    }
    body_right = {
        "command": "右",
        "parameter": "default",
        "commandType": "customzie"
    }
    body_up = {
        "command": "上",
        "parameter": "default",
        "commandType": "customzie"
    }
    body_down = {
        "command": "下",
        "parameter": "default",
        "commandType": "customzie"
    }
    body_enter = {
        "command": "決定",
        "parameter": "default",
        "commandType": "customzie"
    }

    url = this.body_base + "/" + bot_id + "/commands"
    print("url : " + url)
    print("body_up")
    result = requests.post(url, headers=this.post_header, data=json.dumps(body_up))
    time.sleep(1)
    print("body_down")
    result = requests.post(url, headers=this.post_header, data=json.dumps(body_down))
    time.sleep(1)
    print("body_enter")
    result = requests.post(url, headers=this.post_header, data=json.dumps(body_enter))
    time.sleep(1)
