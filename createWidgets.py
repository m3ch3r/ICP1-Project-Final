from tkinter import filedialog
import tkinter
from tkinter.constants import DISABLED, END, NORMAL
from calcTest import evalInput

def insertIntoTextBox(textBox, insertVal):
    textBox["state"] = NORMAL
    textBox.insert(END, str(insertVal))
    textBox["state"] = DISABLED

def clearTextBox(textBox):
    textBox["state"] = NORMAL
    textBox.delete('1.0', END)
    textBox["state"] = DISABLED

def createCalcButtons(app, textBox):
    # numpad
    bInt1 = tkinter.Button(app, text = str(1), width = 2, command = lambda: insertIntoTextBox(textBox, 1)).place(x = 600, y = 375)
    bInt2 = tkinter.Button(app, text = str(2), width = 2, command = lambda: insertIntoTextBox(textBox, 2)).place(x = 625, y = 375)
    bInt3 = tkinter.Button(app, text = str(3), width = 2, command = lambda: insertIntoTextBox(textBox, 3)).place(x = 650, y = 375)
    bInt4 = tkinter.Button(app, text = str(4), width = 2, command = lambda: insertIntoTextBox(textBox, 4)).place(x = 600, y = 350)
    bInt5 = tkinter.Button(app, text = str(5), width = 2, command = lambda: insertIntoTextBox(textBox, 5)).place(x = 625, y = 350)
    bInt6 = tkinter.Button(app, text = str(6), width = 2, command = lambda: insertIntoTextBox(textBox, 6)).place(x = 650, y = 350)
    bInt7 = tkinter.Button(app, text = str(7), width = 2, command = lambda: insertIntoTextBox(textBox, 7)).place(x = 600, y = 325)
    bInt8 = tkinter.Button(app, text = str(8), width = 2, command = lambda: insertIntoTextBox(textBox, 8)).place(x = 625, y = 325)
    bInt9 = tkinter.Button(app, text = str(9), width = 2, command = lambda: insertIntoTextBox(textBox, 9)).place(x = 650, y = 325)
    bInt0 = tkinter.Button(app, text = str(0), width = 2, command = lambda: insertIntoTextBox(textBox, 0)).place(x = 625, y = 400)

    # action buttons 
    bActEq = tkinter.Button(app, text = "=", width = 3, command = lambda: insertIntoTextBox(textBox, "=")).place(x = 675, y = 350)
    bActX1 = tkinter.Button(app, text = "*x", width = 3, command = lambda: insertIntoTextBox(textBox, "*x")).place(x = 675, y = 375)
    bActX2 = tkinter.Button(app, text = "x", width = 3, command = lambda: insertIntoTextBox(textBox, "x")).place(x = 715, y = 375)
    bActSin = tkinter.Button(app, text = "sin(", width = 3, command = lambda: insertIntoTextBox(textBox, "sin(")).place(x = 675, y = 400)
    bActClosePara = tkinter.Button(app, text = ")", width = 3, command = lambda: insertIntoTextBox(textBox, ")")).place(x = 715, y = 400)
def openFile():
    file = filedialog.askopenfile(filetypes =[('Python Graphing Calculator Files', '*.pygraph')])
    content = file.read()
    content = content.split(";")
    
    

def createTxtBtns(app, turtle):
    sbx = 501
    text = tkinter.Text(app, width = 12, height = 2, state = DISABLED)
    text.place(x = sbx + 3, y = 100)
    clr = tkinter.Button(app, height = 2, width = 3, text = "CLR", command = lambda: clearTextBox(text)).place(x = sbx + 150, y = 100)
    ref = tkinter.Button(app, height = 2, width = 10, text = "Refresh/Draw", command = lambda: evalInput(text.get("1.0","end"), turtleWindow = turtle, color = "blue")).place(x = sbx + 180, y = 100)
    createCalcButtons(app, text)

def createMenuBar(app, saveFunction, newFunction, openFunction):
    menuBar = tkinter.Menu(app)
    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command = newFunction)
    fileMenu.add_command(label="Open", command = openFile)
    fileMenu.add_command(label="Save", command = saveFunction)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command = app.quit)
    menuBar.add_cascade(label="File", menu = fileMenu)
    app.config(menu=menuBar)



