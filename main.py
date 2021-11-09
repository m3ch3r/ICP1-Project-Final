from gridDraw import *
from createWidgets import *
from calcTest import *

from tkinter import messagebox
import tkinter

def donothing():
    print("not implemented lol")

def main():
    app = tkinter.Tk()
    app.wm_iconbitmap('logo.ico')
    app.title("Graphing Calculator")
    app.geometry("800x500")
    messagebox.showinfo(title = "Notice", message = "This is a reminder that when formatting equations to make it the full equation. You cannot put for example 1x + 3, it must be formatted like 1*x+3.")

 
    t = drawGridOnWindow(app)
    createTxtBtns(app, t)

    app.mainloop()
main()