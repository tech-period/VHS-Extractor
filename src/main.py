from light_capture.service import service as lc_service
from switchbot.service import service as sb_service

def main():
    # 各サービスをインスタンス化
    lc_srv = lc_service()
    sb_srv = sb_service()

    # LightCaptureを起動
    lc_srv.stard_light_capture()

    # 設定画面を開く
    # lc_srv.open_settings()

    # 録画開始
    lc_srv.start_rec()

    # 保存先を変更
    # path = str("C:\\Users\\goter\\Videos\\Captures")
    # lc_srv.change_destination(path)

    # Switchbotを操作
    sb_srv.execute_command("power", 15)

    sb_srv.execute_command("power", 10)

    # 録画の自動終了を監視
    if lc_srv.check_end_rec():
        # アプリを閉じる
        lc_srv.exit()

# root method
if __name__ == "__main__":
    main()
