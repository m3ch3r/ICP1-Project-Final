from gridDraw import *
import tkinter

def main():
    sbx = 501
    app = tkinter.Tk()
    app.geometry("750x500")

    text1 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 20)
    btn1 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 20)

    text2 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 60)
    btn2 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 60)

    text2 = tkinter.Text(app, height = 2, width = 20).place(x = sbx, y = 100)
    btn3 = tkinter.Button(app, height = 2, width = 3, text = "CLR").place(x = sbx + 150, y = 100)

    t = drawGridOnWindow(app)
    app.mainloop()
main()