import json
import requests

from asset import token as t

class service():
    def __init__(self):
        self.body_base = "https://api.switch-bot.com/v1.0/devices"
        self.header = {"Authorization" : t.token_id}
        self.response = requests.get(self.body_base, headers=self.header)        
        self.devices  = json.loads(self.response.text)

        # Get switchbot bot "deviceId" in all device information
        self.bots_id  = [device["deviceId"] for device in self.devices['body']['deviceList']]

this = service()

# Get all switchbot bot power state and output on your display
for bot_id in this.bots_id:
 
    response = requests.get("https://api.switch-bot.com/v1.0/devices/" + bot_id + "/status", headers=this.header)
    bot      = json.loads(response.text)

    print("bot id : " + bot_id)


