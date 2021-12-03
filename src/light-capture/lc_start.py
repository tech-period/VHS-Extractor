import subprocess as sp

class lc_start():

    # デフォルトのインストールパス
    path = "C:\\Program Files (x86)\\I-O DATA\\LightCapture\\LightCapture.exe"

    def stard_light_capture():
        print(lc_start().path)
        sp.Popen(lc_start().path)

# debug用
# lc_start.stard_light_capture()