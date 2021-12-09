class commands():

    def __init__(self) -> None:
        self.command_list = {
        # <python側の呼び名>：<Andrroidアプリ側で設定したボタン名>
        # 基本コマンド
        "power" : "電源",
        "home" : "ホーム",
        "enter" : "決定",
        # 矢印コマンド
        "up" : "上",
        "down" : "下",
        "right" : "右",
        "left" : "左",
    }

    def get_command(self, command_name:str):        
        result = {
            "command": self.command_list[command_name],
            "parameter": "default",
            "commandType": "customzie"
        }
        return result