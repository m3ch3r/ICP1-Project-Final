from turtle import *
from turtle import Canvas
import tkinter as tk

def drawGrid(t):
    t.speed(-1)
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.right(90)
    t.forward(500)
    t.penup()
    t.goto(250, 0)
    t.right(90)
    t.pendown()
    t.forward(500)

def drawGridOnWindow(rootWindow):
    turtleCanvas = Canvas(master = rootWindow, bg = "black", height = 500, width = 500)
    turtleCanvas.place(x = 0, y = 0) # not to be confused with the grid being drawn (is used to position the canvas)
    global t
    t=RawTurtle(turtleCanvas)
    drawGrid(t)
    return t

