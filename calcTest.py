from math import sin


def evalInput(equationIn, turtleWindow, color):
        turtleWindow.color(color)
        turtleWindow.penup()
        turtleWindow.goto(0, 0)
        turtleWindow.forward(2)
        equationOut1 = equationIn.replace("x", str(-100))
        equationOut1 = eval(equationOut1)
        turtleWindow.goto(10, equationOut1 * 10)
        turtleWindow.pendown()
        for x in range(-99, 100):
            equationOut = equationIn.replace("x", str(x))
            equationOut = eval(equationOut)
            print("old", str(x*10))
            print("scaled",str(x))
            turtleWindow.goto(x *10, equationOut * 10)




