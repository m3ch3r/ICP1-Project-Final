import tkinter
from tkinter import END
from calcTest import evalLinear

def createTxtBtns(app, turtle):
    sbx = 501
    text1 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 20)
    clr1 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 20)

    text2 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 60)
    clr2 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 60)

    text3 = tkinter.Entry(app, width = 20)
    text3.place(x = sbx, y = 100)
    clr3 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 100)
    ref3 = tkinter.Button(app, height = 2, width = 10, text = "Refresh/Draw", command = lambda: evalLinear(text3.get(), turtleWindow = turtle)).place(x = sbx + 180, y = 100)


def createMenuBar(app, saveFunction, newFunction, openFunction):
    menuBar = tkinter.Menu(app)
    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command = newFunction)
    fileMenu.add_command(label="Open", command = openFunction)
    fileMenu.add_command(label="Save", command = saveFunction)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command = app.quit)
    menuBar.add_cascade(label="File", menu = fileMenu)
    app.config(menu=menuBar)