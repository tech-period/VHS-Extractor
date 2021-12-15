import tkinter
from tkinter import Tk, ttk as ttk

class view():
    chk_flag = [True,False]
    def get_state(self, bool:bool) -> str:
        return 'normal' if bool else 'disabled'

    def __init__(self) -> None:
        # ウィンドウの作成
        win = tkinter.Tk()
        win.title('VHS Extractor')

        # オブジェクトの定義
        label_drive = tkinter.Label(win, text='保存先ドライブ', justify='left')
        chk_box_state = [tkinter.BooleanVar(),tkinter.BooleanVar()]
        self.label_title = [tkinter.Label(win),tkinter.Label(win)]
        self.entry_box = [tkinter.Entry(),tkinter.Entry()]
        for i in range(2):
            chk_box_state[i].set(self.chk_flag[i])
            self.label_title[i].config(text='タイトル', justify='left', state=self.get_state(self.chk_flag[i]))
            self.entry_box[i].config(state=self.get_state(self.chk_flag[i]))

        # チェックボタン押下時処理
        def change_state(num:int,bool:bool):
            self.label_title[num].config(state=self.get_state(bool))
            self.entry_box[num].config(state=self.get_state(bool))

        # サイズ設定(16:9)
        win_size = [520,270]
        def get_center_position():
            def calc(a:int,b:int) -> int: return int((a-b)/2)
            w = calc(win.winfo_screenwidth(), win_size[0])
            h = calc(win.winfo_screenheight(), win_size[1])
            return [w,h]

        win.geometry(
            "{0[0]}x{0[1]}+{0[2]}+{0[3]}"
            .format(win_size + get_center_position())
            )
        
        # 画面構成
        pos = [0,0]
        label_drive.grid(row=pos[0], column=pos[1], padx= 10, pady= 10, sticky=tkinter.W)
        
        pos = [1,0]
        # ドロップダウンボックス
        disp_data = ('C:', 'D:', 'L:')
        # ドライブが１つしか該当しない場合はstate='disable'に変更
        state = 'disable' if False else 'readonly'
        dropdown_box = ttk.Combobox(win, values=disp_data, width=5, state=state)
        dropdown_box.current(0)
        dropdown_box.grid(row=pos[0], column=pos[1], padx= 10, sticky=tkinter.W)

        # ToDo -> チェックボックスの状態に応じてstateを調整する
        # １列目
        pos=[2,0]
        chkbox = tkinter.Checkbutton(win, text='8mm, miniDV', variable=chk_box_state[0], command=lambda: change_state(int(0),chk_box_state[0].get()))
        chkbox.grid(row=pos[0], column=pos[1], padx=10, pady= (20,0), sticky=tkinter.W)

        pos = [3,0]
        self.label_title[0].grid(row=pos[0], column=pos[1], padx= 5, sticky=tkinter.W)

        pos = [4,0]
        self.entry_box[0].grid(row=pos[0], column=pos[1], padx= 10, sticky=tkinter.W)

        # ２列目
        pos = [2,1]
        chkbox = tkinter.Checkbutton(win, text='VHS', variable=chk_box_state[1], command=lambda: change_state(int(1), chk_box_state[1].get()))
        chkbox.grid(row=pos[0], column=pos[1], padx=(10,0), pady= (20,0), sticky=tkinter.W)

        pos = [3,1]
        self.label_title[1].grid(row=pos[0], column=pos[1], padx= 5, sticky=tkinter.W)

        pos = [4,1]
        self.entry_box[1].grid(row=pos[0], column=pos[1], padx= (10,0), sticky=tkinter.W)

        # ToDo -> 8mmとVHSの両方にチェックがついていない場合はstateをdisableに変更する
        pos = [5,0]
        button_exe = tkinter.Button(win, text="実行", width=20, state='normal', command=self.exe_app)
        button_exe.grid(row=pos[0], column=pos[1], padx=5, pady= 15, sticky=tkinter.W)

        # ウィンドウのループ処理
        win.mainloop()

    # イベント処理
    def exe_app(self):
        print("exe app")

