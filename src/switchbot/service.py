import requests

from asset import token

class service():

    BODY_BASE = "https://api.switch-bot.com/v1.0/devices"
    HEADER = {"Authorization" : token.token_id}

    response = any

    def __init__():
        service.response = requests.get(service.BODY_BASE, headers=service.HEADER)
        


