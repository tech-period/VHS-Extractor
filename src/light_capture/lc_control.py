import pyautogui as gui
import time
from .asset.dic import dic

class lc_control():

    # 録画開始
    def start_rec():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("rec"))
            gui.click(x,y)
        except Exception as e:
            lc_control.find_nothing(e)

    # 録画終了
    def stop_rec():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("stop"))
            gui.click(x,y)
        # except gui.raisePyAutoGUIImageNotFoundException as e:
        #     print()
        except Exception as e:
            lc_control.find_nothing(e)

    # 設定を開く
    def open_settings():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("setting"))
            gui.click(x,y)
            # ダイアログが開くため、1秒待機
            time.sleep(1)
        except Exception as e:
            lc_control.find_nothing(e)

    # 保存先を変更
    def change_destination(destination):
        try:
            # print(destination)
            x,y = gui.locateCenterOnScreen(dic.get("destination"))
            gui.click(x+200,y)
            gui.hotkey('ctrl', 'a')
            gui.write(destination)

            # debug時はキャンセルボタンを押す
            # x,y = gui.locateCenterOnScreen(dic.get("ok"))
            x,y = gui.locateCenterOnScreen(dic.get("cancel"))
            gui.click(x,y)
            
        except Exception as e:
            lc_control.find_nothing(e)

    # ボタン検出失敗時
    def find_nothing(e):
        print("対象が見つかりませんでした")
        print(e)



# debug用
# lc_control.open_settings()
# path = str("C:\\Users\\goter\\Videos\\Captures")
# lc_control.change_destination(path)
# lc_control.start_rec()
# lc_control.stop_rec()