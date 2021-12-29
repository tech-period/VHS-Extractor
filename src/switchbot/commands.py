class commands():

    def __init__(self) -> None:
        # <python側の呼び名>：<Andrroidアプリ側で設定したボタン名>
        self.command_list = {

        # ビデオデッキ
        "power" : "電源",
        "play" : "再生",
        "pause" : "一時停止",
        "stop" : "停止",
        "back" : "巻き戻し",
        "video8" : "Video8",
        "vhs" : "VHS",
        "reject" : "取り出し",
    }

    def get_command(self, command_name:str):        
        result = {
            "command": self.command_list[command_name],
            "parameter": "default",
            "commandType": "customzie"
        }
        return result