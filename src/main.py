import time

from light_capture.lc_app_manage import lc_app_manage
from light_capture.lc_control import lc_control

def main():

    # LightCaptureを起動
    lc_app_manage.stard_light_capture()

    print("wait 3 sec")
    time.sleep(3)

    # LightCaptureを起動
    lc_control.open_settings()

    # 保存先を変更
    path = str("C:\\Users\\goter\\Videos\\Captures")
    lc_control.change_destination(path)

    # アプリを閉じる
    lc_control.exit()

if __name__ == "__main__":
    main()
