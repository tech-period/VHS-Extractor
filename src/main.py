from logging import basicConfig, Formatter, FileHandler, StreamHandler, DEBUG, INFO, WARNING
from logging import getLogger

from core.view import view as v
from core.service import service as core_service
from light_capture.service import service as lc_service
from line_bot.service import service as lb_service
from switchbot.service import service as sb_service

# ログ設定
stream_handler = StreamHandler()
stream_handler.setFormatter(Formatter('[%(levelname)s]%(message)s'))
file_handler = FileHandler(f"logs.log",encoding='utf-8')
file_handler.setFormatter(Formatter('%(asctime)s:[%(levelname)s]%(message)s'))
basicConfig(handlers=[stream_handler,file_handler], level=DEBUG)
logger = getLogger(__name__)

def main():
    # 各サービスをインスタンス化
    view = v()    
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
    
    # 各サービスをインスタンス化
    view = v()
    core_srv = core_service()
    lc_srv = lc_service()
    # sb_srv = sb_service()
    # lb_srv = lb_service()

    # LightCaptureを起動
    lc_srv.stard_light_capture()

    # light captureの起動を確認
    if lc_srv.check_run() == False:
        # lb_srv.push_message("Light Captureアプリの起動に失敗しました"
        #                     +"\n以下の状態を確認してください"
        #                     +"\n・機器に接続されているかどうか"
        #                     +"\n・画面上にアプリの画面がない（設定ボタンが隠れていると認識しません）"
        #                     +"\n・アプリの更新等のメッセージで止まっている")
        exit()

    # 録画開始
    try:
        exe_flag = [view.info['conditions'][i]['check'] for i in range(2)]
        for i in range(2):
            if exe_flag[i] == False: continue
            file_path = core_srv.get_last_file(lc_srv.default_download_path)
            core_srv.copy_made_file(file_path,
                                    view.info['drive'],
                                    view.info['conditions'][i]['type'],
                                    view.info['conditions'][i]['name'])
            # lb_srv.push_message("ビデオの抽出が完了しました"
            #                     +"\nビデオ形式："+view.info['conditions'][i]['type']
            #                     +"\nファイル名："+view.info['conditions'][i]['name'])
            # if i == 0 and exe_flag[i+1]:
            #     lb_srv.push_message("続けて"+view.info['conditions'][i+1]['type']+"の抽出を開始します")
    except Exception as e:
        logger.exception('catched exception')
        # lb_srv.push_message('録画中にエラーが発生したため、アプリが途中で終了しました'
        #                     +'\n管理者にお問い合わせください')
        logger.info('exit application with exception')
        lc_srv.exit()
        exit()

# root method
if __name__ == "__main__":
    logger.info('launch application')
    # main()
    test()
    logger.info('exit application')
