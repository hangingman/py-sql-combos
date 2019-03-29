#!/usr/bin/env python
# -*- coding: utf8 -*-

import tkinter


def do_nothing():
    file_win = tkinter.Toplevel(root)
    button = tkinter.Button(file_win, text="Do nothing button")
    button.pack()


def my_menu_bar(root):
    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=do_nothing)
    filemenu.add_command(label="Open", command=do_nothing)
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_command(label="Save as...", command=do_nothing)
    filemenu.add_command(label="Close", command=do_nothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tkinter.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=do_nothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=do_nothing)
    editmenu.add_command(label="Copy", command=do_nothing)
    editmenu.add_command(label="Paste", command=do_nothing)
    editmenu.add_command(label="Delete", command=do_nothing)
    editmenu.add_command(label="Select All", command=do_nothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=do_nothing)
    helpmenu.add_command(label="About...", command=do_nothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


# ウィンドウ作成
root = tkinter.Tk()
root.title(u"PySQLCombos")
root.geometry("400x300")
my_menu_bar(root)

# メインループ
root.mainloop()



