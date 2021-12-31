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

            "mov_format_category" : "movie_format_category.png",
            "selected_s_term" : "selected_s_terminal.png",
            "selected_composite" : "selected_composite.png",
            "other_category" : "other_category.png",
            "disp_front" : "display_on_the_front.png",
            "text_disp_front" : "text_display_on_the_front.png",
        }

    # getter
    def get(self, name:str) -> str:
        return self.__asset_path + self.__dic[name]