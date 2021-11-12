"""

Title: Python Graphing Calculator
Author: Braden Franklin
Class: Mrs. Woldseth ICP1 Tri 1 2021
Description: A Graphing coded in python that utilizes both turtle and tkinter

"""

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
    app.resizable(False, False)

 
    t = drawGridOnWindow(app)
    createTxtBtns(app, t)

    app.mainloop()
main()