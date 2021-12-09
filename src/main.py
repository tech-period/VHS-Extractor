from light_capture.service import service as lc_service
from switchbot.service import service as sb_service

def main():
    # 各サービスをインスタンス化
    lc_srv = lc_service()
    # sb_srv = sb_service()

    # LightCaptureを起動
    lc_srv.stard_light_capture()

    # 設定画面を開く
    lc_srv.open_settings()

    # 保存先を変更
    path = str("C:\\Users\\goter\\Videos\\Captures")
    lc_srv.change_destination(path)

    # アプリを閉じる
    lc_srv.exit()

    # Switchbotを操作
    # sb_srv.execute_command("home", 3)
    # sb_srv.execute_command("enter", 1)

# root method
if __name__ == "__main__":
    main()
