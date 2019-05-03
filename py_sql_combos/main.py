#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from paphra_tktable import table as tktable
from tkintertable import TableCanvas, TableModel
from constants import *
import logging.config
import os
import logging
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener
from mysql.MySqlLexer import *
from mysql.MySqlParser import *


class PySqlCombosUI:

    def __init__(self):
        # 解析対象のクエリが入るGUI要素
        self.query_text = None
        # クエリをAntlrで解析した後のAST要素
        self.ast_info = None
        # クエリにつながるテーブル情報
        self.table_list_data = None
        self.table_list_table = None


    def do_nothing(self):
        file_win = tk.Toplevel(root)
        button = tk.Button(file_win, text="Do nothing button")
        button.pack()


    def my_menu_bar(self, root):
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="新規", command=self.do_nothing)
        filemenu.add_command(label="開く", command=self.do_nothing)
        filemenu.add_command(label="保存", command=self.do_nothing)
        filemenu.add_command(label="名前を付けて保存", command=self.do_nothing)
        filemenu.add_command(label="閉じる", command=self.do_nothing)
        menubar.add_cascade(label="ファイル", menu=filemenu)

        config_menu = tk.Menu(menubar, tearoff=0)
        config_menu.add_command(label="設定", command=self.do_nothing)
        menubar.add_cascade(label="設定", menu=config_menu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="このソフトウェアについて", command=self.do_nothing)
        menubar.add_cascade(label="ヘルプ", menu=helpmenu)

        root.config(menu=menubar)


    def my_tab_change_event(self, event):
        # タブ切り替えイベント
        logger = get_logger()
        logger.info('tab changed !')

        # フォームに入力されたクエリを読み取る
        query = self.query_text.get("1.0", tk.END)
        logger.info('query = {}'.format(query))

        # Antlrで解析する
        self.ast_info = AstProcessor(
            logging, BasicInfoListener()
        ).execute(query.upper())

        from pprint import pprint
        pprint(self.ast_info)

        # テーブル情報を更新
        model = self.table_list_table.model

        print("***")
        join_tables = self.ast_info['join_parts']
        join_tables = {
            i: {
                'No': i+1,
                'テーブル物理名': k,
                'テーブル論理名': ''
            } for i, k in enumerate( join_tables )
        }
        pprint(join_tables)

        self.table_list_table.clearData()
        model.importDict(join_tables)
        self.table_list_table.redraw()


    def my_tabs(self, root):
        # ノートブック
        nb = ttk.Notebook(width=640, height=480)

        # タブの作成
        tab1 = tk.Frame(nb)
        tab2 = tk.Frame(nb)
        tab3 = tk.Frame(nb)
        nb.add(tab1, text='クエリ入力', padding=3)
        nb.add(tab2, text='クエリ解析', padding=3)
        nb.add(tab3, text='その他', padding=3)
        nb.bind("<<NotebookTabChanged>>", self.my_tab_change_event)
        nb.pack(expand=1, fill='both')

        # タブ1
        # 入力画面ラベルの設定
        label1_1 = tk.Label(tab1, text="クエリ入力画面", font=("", 16), height=2)
        label1_1.pack(fill="x")

        frame1_1 = tk.Frame(tab1, pady=10)
        frame1_1.pack()
        self.query_text = tk.Text(frame1_1, font=("", 14), width=500, height=100)
        self.query_text.insert(tk.END, SAMPLE_QUERY)
        self.query_text.pack(side="left")

        # タブ2
        # 入力画面ラベルの設定
        label2_1 = tk.Label(tab2, text="テーブル定義", font=("", 16), height=2)
        label2_1.pack(fill="both")

        # from句のテーブル一覧
        def_frame = tk.Frame(tab2, pady=10)
        def_frame.pack(fill="both")

        self.table_list_data = {
            '': {
                'No': 1, 'テーブル物理名': 'employee', 'テーブル論理名': '従業員テーブル'
            }
        }
        self.table_list_table = TableCanvas(def_frame,
                                            width=500,
                                            height=100,
                                            editable=False,
                                            data=self.table_list_data)
        self.table_list_table.show()

        label2_2 = tk.Label(tab2, text="データパターン", font=("", 16), height=2)
        label2_2.pack(fill="both")

        # データパターンの入力（仮）
        pattern_frame = tk.Frame(tab2, pady=10)
        pattern_frame.pack(fill="both")

        data = {
            '1': {
                'emp_no': 'null'
            },
            '2': {
                'emp_no': '9999'
            },
        }

        table = TableCanvas(pattern_frame,
                            width=500,
                            height=100,
                            editable=False,
                            data=data)
        table.show()


def get_logger():
    project_dir = os.path.dirname(os.path.abspath('__file__'))
    logging_setting_path = os.path.join(project_dir, 'resources', 'logging', 'utiltools_log.conf')
    logging.config.fileConfig(logging_setting_path)
    return logging.getLogger('outputLogging')


if __name__ == '__main__':
    logger = get_logger()
    # ウィンドウ作成
    root = tk.Tk()
    root.title(u"PySQLCombos")
    root.geometry("640x480")

    py_sql_combo = PySqlCombosUI()
    py_sql_combo.my_menu_bar(root)
    py_sql_combo.my_tabs(root)

    # メインループ
    logger.info('PySQLCombos start !')
    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            # OSXでの不具合対策
            # https://stackoverflow.com/questions/16995969/inertial-scrolling-in-mac-os-x-with-tkinter-and-python
            pass
