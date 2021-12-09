import pyautogui as gui
import time
import subprocess as sp

from .dic import dic

class service():

    def __init__(self) -> None:
        # 操作一覧モデルをインスタンス化
        self.dic = dic()
        # デフォルトのアプリインストールパス
        self.app_path = "C:\\Program Files (x86)\\I-O DATA\\LightCapture\\LightCapture.exe"

    # アプリを起動
    def stard_light_capture(self):
        print("LightCaptureを起動")
        try:
            sp.Popen(self.app_path)
            # sp.Popen(self.app_path + "z")
        except Exception as e:
            print(e)
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
        self.__click_button("destination",add_x=200, add_y=0)
        gui.hotkey('ctrl', 'a')
        gui.write(destination)
        self.__click_button("cancel")

    # アプリを閉じる
    def exit(self):
        self.__click_button("exit")

    # ボタンをクリックする
    def __click_button(self, key:str, try_count:int = 3, add_x:int = 0, add_y:int = 0):
        for tryCount in range(try_count):
            tryCount += 1
            print("try " + key + " button [" + str(tryCount) + "]")
            try:
                x,y = gui.locateCenterOnScreen(self.dic.get(key),grayscale=True)
                print("click "+key+" button")
                gui.click(x+add_x, y+add_y)
                break
            except Exception as e:
                if(tryCount < try_count):
                    print("button is not found. wait a sec")
                    time.sleep(1)
                    continue
                else:
                    self.__find_nothing()

    # ボタン検出失敗時
    def __find_nothing(self):
        print("タイムアウト：対象が見つかりませんでした")
