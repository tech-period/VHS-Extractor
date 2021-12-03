import subprocess as sp

class lc_app_manage():

    # デフォルトのインストールパス
    path = "C:\\Program Files (x86)\\I-O DATA\\LightCapture\\LightCapture.exe"

    def stard_light_capture():
        print(lc_app_manage().path)
        sp.Popen(lc_app_manage().path)

# debug用
# lc_start.stard_light_capture()