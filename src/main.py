import time

from light_capture.lc_app_manage import lc_app_manage
from light_capture.lc_control import lc_control

def main():

    # LightCaptureを起動
    lc_app_manage.stard_light_capture()

    print("wait a sec")
    time.sleep(1)

    # LightCaptureを起動
    lc_control.open_settings()

    # 保存先を変更
    path = str("C:\\Users\\goter\\Videos\\Captures")
    lc_control.change_destination(path)

if __name__ == "__main__":
    main()
