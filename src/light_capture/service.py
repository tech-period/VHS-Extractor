from logging import getLogger

import os
import sys
import time
import subprocess as sp
import pyautogui as gui

from .dic import dic

class service():

    def __init__(self) -> None:
        self.logger = getLogger(__name__)
        # 操作一覧モデルをインスタンス化
        self.dic = dic()
        # デフォルトのアプリインストールパス
        self.app_path = "C:\\Program Files (x86)\\I-O DATA\\LightCapture\\LightCapture.exe"
        self.default_download_path = os.environ['USERPROFILE']+"\\Videos\\LightCapture"

    # アプリを起動
    def stard_light_capture(self):
        self.logger.info("LightCaptureを起動")
        try:
            sp.Popen(self.app_path)
            self.logger.info("wait 3 sec")
            time.sleep(3)
        except Exception as e:
            self.logger.info(e)
            sys.exit(0)

    # アプリの起動確認
    def check_run(self) -> bool:
        self.logger.info("check startup")
        result = False
        # 画面上に設定ボタンがあるかどうかで起動を判定
        try:
            x,y = gui.locateCenterOnScreen(self.dic.get("setting"))
            self.logger.info("startup succeeded")
            result = True
        except:
            self.logger.error("startup failed")
        return result

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

    # 録画終了を監視
    def check_end_rec(self, try_count:int = 3600) -> bool:
        for tryCount in range(try_count):
            tryCount += 1
            self.logger.info("checking the end of recording [" + str(tryCount) + "]")
            try:
                x,y = gui.locateCenterOnScreen(self.dic.get("finished"))
                self.logger.info("detected the end of recording")
                break
            except Exception as e:
                if(tryCount < try_count):
                    self.logger.info("recording...")
                    time.sleep(9)
                    continue
                else:
                    self.logger.info(e)
                    return False
        return True

    # ボタンをクリックする
    def __click_button(self, key:str, try_count:int = 3, add_x:int = 0, add_y:int = 0):
        for tryCount in range(try_count):
            tryCount += 1
            self.logger.info("try " + key + " button [" + str(tryCount) + "]")
            try:
                x,y = gui.locateCenterOnScreen(self.dic.get(key))
                self.logger.info("click "+key+" button")
                gui.click(x+add_x, y+add_y)
                break
            except Exception as e:
                if(tryCount < try_count):
                    self.logger.info("button is not found. wait a sec")
                    time.sleep(1)
                    continue
                else:
                    self.__find_nothing()

    # ボタン検出失敗時
    def __find_nothing(self):
        self.logger.info("タイムアウト：対象が見つかりませんでした")
