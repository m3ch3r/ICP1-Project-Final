from math import sin
from math import cos
from math import pi
from math import sqrt
from math import e
from math import tan

def evalInput(equationIn, turtleWindow, color):
        turtleWindow.speed(-1)
        turtleWindow.color(color)
        turtleWindow.penup()
        turtleWindow.goto(0, 0)
        equationOut1 = equationIn.replace("x", "("+ str(-30 * 10) + ")")
        equationOut1 = eval(equationOut1)
        turtleWindow.goto(-30 * 10, equationOut1 * 10)
        turtleWindow.pendown()
        
        for x in range(-30, 30):
            equationOut = equationIn.replace("x", "(" + str(x) + ")")
            equationOut = eval(equationOut)
            print("old", str(x*10))
            print("scaled",str(x))
            turtleWindow.goto(x *10, equationOut * 10)
        



