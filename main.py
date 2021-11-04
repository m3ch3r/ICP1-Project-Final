from gridDraw import *
from createWidgets import *
from actions import *
from calcTest import *

import tkinter

def donothing():
    print("not implemented lol")

def main():
    app = tkinter.Tk()
    app.wm_iconbitmap('logo.ico')
    app.title("Graphing Calculator")
    app.geometry("800x500")

 
    t = drawGridOnWindow(app)
    createMenuBar(app = app, saveFunction = donothing, newFunction = donothing, openFunction = donothing)
    createTxtBtns(app, t)

    app.mainloop()
main()