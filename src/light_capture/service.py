import pyautogui as gui
import time
import subprocess as sp

from .asset.dic import dic

class service():

    def __init__(self) -> None:
        # 操作一覧モデルをインスタンス化
        self.dic = dic()
        # デフォルトのアプリインストールパス
        self.app_path = "C:\\Program Files (x86)\\I-O DATA\\LightCapture\\LightCapture.exe"

    # アプリを起動
    def stard_light_capture(self):
        print("LightCaptureを起動")
        sp.Popen(self.app_path)
        print("wait 3 sec")
        time.sleep(3)

    # 録画開始
    def start_rec(self):
        self.__click_button("rec")

    # 録画終了
    def stop_rec(self):
        self.__click_button("stop")

    # 設定を開く
    def open_settings(self):
        self.__click_button("setting")
        # ダイアログが開くため１秒待機
        time.sleep(1)

    # 保存先を変更
    def change_destination(self, destination):
        self.__click_button("destination", 200, 0)
        gui.hotkey('ctrl', 'a')
        gui.write(destination)
        self.__click_button("cancel")

    # アプリを閉じる
    def exit(self):
        self.__click_button("exit")

    # ボタンをクリックする
    def __click_button(self, key:str, add_x:int = 0, add_y:int = 0):
        try:
            x,y = gui.locateCenterOnScreen(self.dic.get(key))
            print("click "+key+" button")
            gui.click(x+add_x, y+add_y)
        except Exception as e:
            self.__find_nothing(e)

    # ボタン検出失敗時
    def __find_nothing(e):
        print("対象が見つかりませんでした")
        print(e)

# debug用
# lc_control.open_settings()
# path = str("C:\\Users\\goter\\Videos\\Captures")
# lc_control.change_destination(path)
# lc_control.start_rec()
# lc_control.stop_rec()