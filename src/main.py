from core.view import view as v
from core.service import service as core_service
from light_capture.service import service as lc_service
from line_bot.service import service as lb_service
from switchbot.service import service as sb_service

def main():
    view = v()
    if not view.exe_flag:
        print("実行せずに終了")
        exit()
    
    # 各サービスをインスタンス化
    core_srv = core_service()
    lc_srv = lc_service()
    sb_srv = sb_service()
    lb_srv = lb_service()

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

    lb_srv.push_message("VHSのデータ化が完了しました")

def test():
    # view = v()
    # if view.exe_flag == False:
    #     print("実行せずに終了")
    #     exit()
        
    # print("Appを実行")
    
    # 各サービスをインスタンス化
    core_srv = core_service()
    # lc_srv = lc_service()
    # sb_srv = sb_service()
    # lb_srv = lb_service()

    # ダウンロードフォルダ内で最後に作成されたファイルをコピー
    file_path = core_srv.get_last_file("C:\\Users\\goter\\Downloads")
    core_srv.copy_made_file(file_path, "D:", "8mm")
    # lb_srv.push_message("おテストおメッセージその１")
    # lb_srv.push_message("おテストおメッセージその２")

# root method
if __name__ == "__main__":
    # main()
    test()
