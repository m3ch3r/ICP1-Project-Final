import tkinter

def createTxtBtns(app):
    sbx = 501
    text1 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 20)
    btn1 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 20)

    text2 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 60)
    btn2 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 60)

    text2 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 100)
    btn3 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 100)

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