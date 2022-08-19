from cgitb import text
from email import message
from struct import pack
import tkinter
from tkinter import Button, StringVar, ttk

#インスタンス引数に食材辞書を設定できるようにする
#各フレームで3~4つboxを増やす。一日食べるもの大体決まってるから、
# nosh枠,ヨーグルト枠,サプリ枠などでまとめてしまうとよいかも
#自分の除脂肪体重を入れて、導き出された目標値を各フレームに表示する
#PFCの評価基準を作る　例）評価A,評価B,評価Cなど
#noshの脂質とか普段計算してないから便利かも。

class Application1(ttk.Frame):

    #self.dict = 引数に辞書を指定するには？

    def __init__(self):
        super().__init__(root,
         width=420,height=200,
         borderwidth=4,relief='groove')
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        self.dict = {'プロテイン':24, 'オイコス':12, 'nosh':25, '卵':6}
        self.combobox = ttk.Combobox(self, values=list(self.dict.keys()))
        self.combobox.pack()

        num = range(1,11)
        self.combobox_num = ttk.Combobox(self, values=list(num))
        self.combobox_num.pack()

        self.message = tkinter.Message(self)
        self.message.pack()

        add_btn = tkinter.Button(self, text='add', command=self.calc)
        add_btn.pack()

        clear_btn=tkinter.Button(self, text='clear', command=self.clear)
        clear_btn.pack()

    def calc(self):
        self.result = self.dict[self.combobox.get()]* int(self.combobox_num.get())
        self.message['text'] = str(self.result)

    def clear(self):
        if self.message != None:
            self.message['text']=''

class Application2(ttk.Frame):
    def __init__(self):
        super().__init__(root,
         width=420,height=200,
         borderwidth=4,relief='groove')
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        self.message = tkinter.Message(self)
        self.message.pack()

        pfc_btn = tkinter.Button(self, text='PFC計算', command=self.pfc_calc)
        pfc_btn.pack()
        
    def pfc_calc(self):
        if 102 <= int(protein.message['text']) <= 153 and \
            34 <= int(fat.message['text']) <= 45 and \
            255 <= int(carbo.message['text']) <= 332:
            self.message['text'] = 'OK'
        else:
            self.message['text'] = 'NO'

root = tkinter.Tk()
root.title('PFC計算')
root.geometry('500x700')

protein = Application1()
fat = Application1()
carbo = Application1()
pfc = Application2()

root.mainloop()