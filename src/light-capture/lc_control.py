import pyautogui as gui
from asset import dic

class lc_control():
    # 録画開始
    def start_rec():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("rec"))
            gui.click(x,y)
        except Exception as e:
            find_nothing(e)

    # 録画終了
    def stop_rec():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("stop"))
            gui.click(x,y)
        except gui.raisePyAutoGUIImageNotFoundException as e:
            print()
        except Exception as e:
            find_nothing(e)

    # 設定を開く
    def open_settings():
        try:
            x,y = gui.locateCenterOnScreen(dic.get("setting"))
            gui.click(x,y)
        except gui.raisePyAutoGUIImageNotFoundException as e:
            print()
        except Exception as e:
            find_nothing(e)

    # ボタン検出失敗時
    def find_nothing(e):
        print("対象が見つかりませんでした")
        print(e)


# debug用
lc_control.open_settings()
# lc_control.start_rec()
# lc_control.stop_rec()