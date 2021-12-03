import pyautogui as gui

path = "./src/light-capture/asset/rec_button.png"

class lc_control():
    def start_rec():
        try:
            x,y = gui.locateCenterOnScreen(path)
            gui.doubleClick(x,y)
        except Exception as e:
            print("対象が見つかりませんでした。")
            print(e)


# lc_control.start_rec()