class dic():

    def __init__(self) -> None:
        self.__asset_path = "./src/light_capture/asset/"
        self.__dic = {
            # 操作名：対応画像
            "rec" : "rec_button.png",
            "stop" : "stop_button.png",
            "finished" : "finished_rec_button.png",
            "setting" : "setting_button.png",
            "destination" : "destination.png",
            "ok" : "ok_button.png",
            "cancel" : "cancel_button.png",
            "exit" : "exit_button.png",
        }

    # getter
    def get(self, name:str) -> str:
        return self.__asset_path + self.__dic[name]