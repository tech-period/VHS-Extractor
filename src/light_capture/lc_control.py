import pyautogui as gui
import time
from .asset.dic import dic

class lc_control():

    # 録画開始
    def start_rec():
        lc_control.click_button("rec")

    # 録画終了
    def stop_rec():
        lc_control.click_button("stop")

    # 設定を開く
    def open_settings():
        lc_control.click_button("setting")
        # ダイアログが開くため１秒待機
        time.sleep(1)

    # 保存先を変更
    def change_destination(destination):
        lc_control.click_button("destination", 200, 0)
        gui.hotkey('ctrl', 'a')
        gui.write(destination)
        lc_control.click_button("cancel")

    # アプリを閉じる
    def exit():
        lc_control.click_button("exit")

    # ボタンをクリックする
    def click_button(key:str, add_x:int = 0, add_y:int = 0):
        try:
            d = dic()
            x,y = gui.locateCenterOnScreen(d.get(key))
            print("click "+key+" button")
            gui.click(x+add_x, y+add_y)
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