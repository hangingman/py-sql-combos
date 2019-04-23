#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
from .constants import *


def do_nothing():
    file_win = tk.Toplevel(root)
    button = tk.Button(file_win, text="Do nothing button")
    button.pack()


def my_menu_bar(root):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="新規", command=do_nothing)
    filemenu.add_command(label="開く", command=do_nothing)
    filemenu.add_command(label="保存", command=do_nothing)
    filemenu.add_command(label="名前を付けて保存", command=do_nothing)
    filemenu.add_command(label="閉じる", command=do_nothing)
    menubar.add_cascade(label="ファイル", menu=filemenu)

    config_menu = tk.Menu(menubar, tearoff=0)
    config_menu.add_command(label="設定", command=do_nothing)
    menubar.add_cascade(label="設定", menu=config_menu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="このソフトウェアについて", command=do_nothing)
    menubar.add_cascade(label="ヘルプ", menu=helpmenu)

    root.config(menu=menubar)


def my_tabs(root):
    # ノートブック
    nb = ttk.Notebook(width=640, height=480)

    # タブの作成
    tab1 = tk.Frame(nb)
    tab2 = tk.Frame(nb)
    tab3 = tk.Frame(nb)
    nb.add(tab1, text='クエリ入力', padding=3)
    nb.add(tab2, text='クエリ解析', padding=3)
    nb.add(tab3, text='その他', padding=3)
    nb.pack(expand=1, fill='both')

    # タブ1
    # 入力画面ラベルの設定
    label1_1 = tk.Label(tab1, text="クエリ入力画面", font=("", 16), height=2)
    label1_1.pack(fill="x")

    frame1_1 = tk.Frame(tab1, pady=10)
    frame1_1.pack()
    entry1_1 = tk.Text(frame1_1, font=("", 14), width=500, height=100)
    entry1_1.insert(tk.END, SAMPLE_QUERY)
    entry1_1.pack(side="left")

    # タブ2
    # 入力画面ラベルの設定
    label2_1 = tk.Label(tab2, text="クエリ解析", font=("", 16), height=2)
    label2_1.pack(fill="x")

    # フレーム2_1の作成
    frame2_1 = tk.Frame(tab2, pady=10)
    frame2_1.pack()

    # リスト2_1の作成
    listb2_1 = tk.Listbox(frame2_1, width=20, height=7)
    listb2_1.pack()

    # スクロール2_1の作成
    scroll2_1 = tk.Scrollbar(frame2_1, orient='v', command=listb2_1.yview)

    # スクロールの設定
    listb2_1.configure(yscrollcommand=scroll2_1.set)

    # gridで配置
    listb2_1.grid(row=1, column=0, sticky='ns')
    scroll2_1.grid(row=1, column=1, sticky='ns')


# ウィンドウ作成
root = tk.Tk()
root.title(u"PySQLCombos")
root.geometry("640x480")
my_menu_bar(root)
my_tabs(root)

# メインループ
root.mainloop()
