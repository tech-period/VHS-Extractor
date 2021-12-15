import tkinter

class view():
    def __init__(self) -> None:
        # ウィンドウの作成
        self.win = tkinter.Tk()
        # 基本項目
        self.win.title('保存先設定')

        # サイズ設定
        self.win_size = [1920,1080]
        self.win.geometry(
            "{0[0]}x{0[1]}+{0[2]}+{0[3]}"
            .format(self.win_size + self.__get_center_position())
            )
        
        # ラベルの追加
        self.label_1 = tkinter.Label(self.win, text='よろしくお願いします')
        self.label_1.pack()

        # ウィンドウのループ処理
        self.win.mainloop()

    def __get_center_position(self):
        def calc(a:int,b:int) -> int: return int((a-b)/2)
        w = calc(self.win.winfo_screenwidth(), self.win_size[0])
        h = calc(self.win.winfo_screenheight(), self.win_size[1])
        return [w,h]