import time

from light_capture.lc_app_manage import lc_app_manage
from light_capture.lc_control import lc_control

def main():
    # 各サービスをインスタンス化
    lc_cnt = lc_control()

    # LightCaptureを起動
    lc_app_manage.stard_light_capture()

    print("wait 3 sec")
    time.sleep(3)

    # LightCaptureを起動
    lc_cnt.open_settings()

    # 保存先を変更
    path = str("C:\\Users\\goter\\Videos\\Captures")
    lc_cnt.change_destination(path)

    # アプリを閉じる
    lc_cnt.exit()

if __name__ == "__main__":
    main()
