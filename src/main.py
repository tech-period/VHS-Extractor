from logging import basicConfig, Formatter, FileHandler, StreamHandler, DEBUG, INFO, WARNING
from logging import getLogger
<<<<<<< HEAD
from sys import exit
import time
import threading
=======
import time
>>>>>>> main

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
basicConfig(handlers=[stream_handler,file_handler], level=INFO)
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
<<<<<<< HEAD
    time.sleep(3)
=======
>>>>>>> main

    # light captureの起動を確認
    if lc_srv.check_run() == False:
        lb_srv.push_message("Light Captureアプリの起動に失敗しました"
                            +"\n以下の状態を確認してください"
                            +"\n・機器に接続されているかどうか"
                            +"\n・画面上にアプリの画面がない（設定ボタンが隠れていると認識しません）"
                            +"\n・アプリの更新等のメッセージで止まっている")
        exit()

<<<<<<< HEAD
    # 初期設定
=======
    # アプリの初期設定
>>>>>>> main
    lc_srv.change_initial_settings()

    # 録画処理
    try:
        exe_flag = [view.info['conditions'][i]['check'] for i in range(2)]
        thread = []
        for i in range(2):
            if exe_flag[i] == False: continue
            # ビデオデッキの準備
            sb_srv.execute_command('video8' if i == 0 else 'vhs', 2)
            sb_srv.execute_command('stop', 2)
<<<<<<< HEAD
            # sb_srv.execute_command('back', 1)
            sb_srv.execute_command('back', 180)
=======
            # sb_srv.execute_command('back', 180)
            sb_srv.execute_command('back', 2)
>>>>>>> main
            sb_srv.execute_command('stop', 2)

            # 録画開始
            sb_srv.execute_command('play', 2)
<<<<<<< HEAD
            print("wait "+ view.info['conditions'][i]['time'] + "min")
            # time.sleep(int(view.info['conditions'][i]['time'])*10)
            time.sleep(int(view.info['conditions'][i]['time'])*60)
            lc_srv.stop_rec()
            sb_srv.execute_command('stop', 2)
=======
            lc_srv.start_rec()

            # 録画終了を監視
            lc_srv.check_end_rec()
>>>>>>> main

            # ファイルコピー（別スレッド）
            j = i
            def file_copy():
                file_path = core_srv.get_last_file(lc_srv.default_download_path)
                core_srv.copy_made_file(file_path,
                                        view.info['drive'],
                                        view.info['conditions'][j]['type'],
                                        view.info['conditions'][j]['name'])
                lb_srv.push_message("ビデオの抽出が完了しました"
                                    +"\nビデオ形式："+view.info['conditions'][j]['type']
                                    +"\nファイル名："+view.info['conditions'][j]['name'])
                if j == 0 and exe_flag[1]:
                    lb_srv.push_message("続けて"+view.info['conditions'][j+1]['type']+"の抽出を開始します")
            thread.append(threading.Thread(target=file_copy))
            thread[i].start()

        # LightCaputureアプリを閉じる
        lc_srv.exit()

        # 両ビデオテープを巻き戻す
        for i in range(2):
            if exe_flag[i] == False: continue
            sb_srv.execute_command('video8' if i == 0 else 'vhs', 5)
            # sb_srv.execute_command('back', 1)
            sb_srv.execute_command('back', 180)
            sb_srv.execute_command('stop', 2)
            sb_srv.execute_command('reject', 5)

        # 終了メッセージを送信
        lb_srv.push_message("全行程が終了しました\nビデオテープを取り出してください")

    # 処理中の例外発生時
    except Exception as e:
        logger.exception('catched exception')
        lb_srv.push_message('録画中にエラーが発生したため、アプリが途中で終了しました'
                            +'\n管理者にお問い合わせください')
        logger.info('exit application with exception')
        lc_srv.exit()
        exit()

def test():
    # 各サービスをインスタンス化
    view = v()
    # core_srv = core_service()
<<<<<<< HEAD
    # lc_srv = lc_service()
    # sb_srv = sb_service()
    # lb_srv = lb_service()

    # 録画処理
    try:
        exe_flag = [view.info['conditions'][i]['check'] for i in range(2)]
        for i in range(2):
            if exe_flag[i] == False: continue
            print("wait "+ view.info['conditions'][i]['time'] + "sec")
            time.sleep(int(view.info['conditions'][i]['time']))
            print('stop')
    # 処理中の例外発生時
    except Exception as e:
        logger.exception('catched exception')
        logger.info('exit application with exception')
        exit()
=======
    lc_srv = lc_service()
    # sb_srv = sb_service()
    # lb_srv = lb_service()

    # 録画終了を監視
    # lc_srv.change_initial_settings()
    lc_srv.check_end_rec()
>>>>>>> main

    pass

# root method
if __name__ == "__main__":
    logger.info('launch application')
    main()
    # test()
    logger.info('exit application')
