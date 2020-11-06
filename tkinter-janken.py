#-*- coding: utf8 -*-
import sys
import Tkinter as tk


root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'じゃんけん')

# ここでウインドウサイズを定義する
root.geometry('400x300')

def rock(event):
    Label1["text"] = "グー"
def scissors(event):
    Label1["text"] = "チョキ"
def paper(event):
    Label1["text"] = "パー"


# ラベルを使って文字を画面上に出す
me = tk.Label(text=u'自分の手:',background='#00cccc')
me.place(x=30,y=30)

Label1 = tk.Label(text=u'手を選択して下さい',
background='#00cccc')
Label1.place(x=100,y=30)

Label2 = tk.Label(text=u'相手の手:',background='#00cccc')
Label2.place(x=30,y=50)


# Buttonを設置してみる
Button1 = tk.Button(text=u'グー', width=10,height=4)
Button1.bind("<Button-1>", rock)        # 左クリックが押されたときに実行される関数をバインドします
Button1.place(x=50,y=200)

Button2 = tk.Button(text=u'チョキ', width=10,height=4)
Button2.bind("<Button-1>", scissors)        # ボタンが押されたときに実行される関数をバインドします
Button2.place(x=150,y=200)

Button3 = tk.Button(text=u'パー', width=10,height=4)
Button3.bind("<Button-1>", paper)        # ボタンが押されたときに実行される関数をバインドします
Button3.place(x=250,y=200)

root.mainloop()