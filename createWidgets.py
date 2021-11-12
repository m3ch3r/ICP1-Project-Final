from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter.constants import DISABLED, END, NORMAL
import turtle
from calcTest import evalInput
from gridDraw import drawGrid


def insertIntoTextBox(textBox, insertVal):
    textBox["state"] = NORMAL
    textBox.insert(END, str(insertVal))
    textBox["state"] = DISABLED

def clearTextBox(textBox):
    textBox["state"] = NORMAL
    textBox.delete('1.0', END)
    textBox["state"] = DISABLED

def clearCanvas(turtleWindow):
    for i in range(2):
        turtleWindow.clear()
        drawGrid(turtleWindow)
        

def createCalcButtons(app, textBox):
    # numpad
    bInt1 = ttk.Button(app, text = str(1), width = 5, command = lambda: insertIntoTextBox(textBox, 1)).place(x = 600, y = 375)
    bInt2 = ttk.Button(app, text = str(2), width = 5, command = lambda: insertIntoTextBox(textBox, 2)).place(x = 645, y = 375)
    bInt3 = ttk.Button(app, text = str(3), width = 5, command = lambda: insertIntoTextBox(textBox, 3)).place(x = 690, y = 375)
    bInt4 = ttk.Button(app, text = str(4), width = 5, command = lambda: insertIntoTextBox(textBox, 4)).place(x = 600, y = 350)
    bInt5 = ttk.Button(app, text = str(5), width = 5, command = lambda: insertIntoTextBox(textBox, 5)).place(x = 645, y = 350)
    bInt6 = ttk.Button(app, text = str(6), width = 5, command = lambda: insertIntoTextBox(textBox, 6)).place(x = 690, y = 350)
    bInt7 = ttk.Button(app, text = str(7), width = 5, command = lambda: insertIntoTextBox(textBox, 7)).place(x = 600, y = 325)
    bInt8 = ttk.Button(app, text = str(8), width = 5, command = lambda: insertIntoTextBox(textBox, 8)).place(x = 645, y = 325)
    bInt9 = ttk.Button(app, text = str(9), width = 5, command = lambda: insertIntoTextBox(textBox, 9)).place(x = 690, y = 325)
    bInt0 = ttk.Button(app, text = str(0), width = 5, command = lambda: insertIntoTextBox(textBox, 0)).place(x = 645, y = 400)

    # action buttons 
    bActEx = ttk.Button(app, text = "^", width = 3, command = lambda: insertIntoTextBox(textBox, "**")).place(x = 740, y = 350)
    bActX = ttk.Button(app, text = "x", width = 3, command = lambda: insertIntoTextBox(textBox, "x")).place(x = 740, y = 375)
    bActSin = ttk.Button(app, text = "sin", width = 3, command = lambda: insertIntoTextBox(textBox, "sin(")).place(x = 740, y = 400)
    bActCos = ttk.Button(app, text = "cos", width = 3, command = lambda: insertIntoTextBox(textBox, "cos(")).place(x = 740, y = 425)
    bActTan = ttk.Button(app, text = "tan", width = 3, command = lambda: insertIntoTextBox(textBox, "tan(")).place(x = 740, y = 450)
    bActClosePara = ttk.Button(app, text = ")", width = 3, command = lambda: insertIntoTextBox(textBox, ")")).place(x = 560, y = 400)
    bActOpenPara = ttk.Button(app, text = "(", width = 3, command = lambda: insertIntoTextBox(textBox, "(")).place(x = 530, y = 400)

    bActAdd = ttk.Button(app, text = "+", width = 3, command = lambda: insertIntoTextBox(textBox, "+")).place(x = 530, y = 440)
    bActMinus = ttk.Button(app, text = "-", width = 3, command = lambda: insertIntoTextBox(textBox, "-")).place(x = 530, y = 465)
    bActDiv = ttk.Button(app, text = "÷", width = 3, command = lambda: insertIntoTextBox(textBox, "/")).place(x = 560, y = 440)
    bActMult = ttk.Button(app, text = "×", width = 3, command = lambda: insertIntoTextBox(textBox, "*")).place(x = 560, y = 465)
    
    bActPi = ttk.Button(app, text = "π", width = 6, command = lambda: insertIntoTextBox(textBox, "pi")).place(x =  530, y = 350)
    bActE = ttk.Button(app, text = "e", width = 6, command = lambda: insertIntoTextBox(textBox, "e")).place(x = 530, y = 375)

    bActSqrt = ttk.Button(app, text = "√", width = 3, command = lambda: insertIntoTextBox(textBox, "sqrt(")).place(x = 740, y = 325)

def openFile(textbox1):
    file = filedialog.askopenfile(filetypes =[('Python Graphing Calculator Files', '*.pygraph')])
    content = file.read()
    content = content.split(";")
    clearTextBox(textbox1)
    insertIntoTextBox(textbox1, content[0])
def createTxtBtns(app, turtle):
    sbx = 501
    text1 = tkinter.Text(app, width = 16, height = 2, state = DISABLED)
    text1.place(x = sbx + 3, y = 100)



    clr = ttk.Button(app, width = 3, text = "CLR", command = lambda: clearTextBox(text1)).place(x = sbx + 150, y = 100)
    ref1 = ttk.Button(app, width = 18, text = "Refresh/Draw", command = lambda: evalInput(text1.get("1.0","end"), turtleWindow = turtle, color = "blue")).place(x = sbx + 180, y = 100)
    ref2 = ttk.Button(app, width = 18, text = "Clear Graph", command = lambda: clearCanvas(turtle)).place(x = sbx + 180, y = 75)
    createCalcButtons(app, text1)
    createMenuBar(app, text1)

def createMenuBar(app, text1):
    menuBar = tkinter.Menu(app)
    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Open", command = lambda: openFile(text1))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command = app.quit)
    menuBar.add_cascade(label="File", menu = fileMenu)
    app.config(menu=menuBar)



