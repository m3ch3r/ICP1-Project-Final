from gridDraw import *
from createWidgets import *
import tkinter

def donothing():
    print("not implemented lol")

def main():
    app = tkinter.Tk()
    app.wm_iconbitmap('logo.ico')
    app.title("Graphing Calculator")
    app.geometry("750x500")

    createMenuBar(app = app, saveFunction = donothing, newFunction = donothing, openFunction = donothing)
    createTxtBtns(app)
    t = drawGridOnWindow(app)


    app.mainloop()
main()