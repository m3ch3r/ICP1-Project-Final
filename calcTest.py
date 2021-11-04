import math

def evalLinear(equationIn, turtleWindow):
    turtleWindow.penup()
    turtleWindow.goto(0, 0)
    turtleWindow.forward(2)
    equationOut1 = equationIn.replace("x", "*" + str(1))
    equationOut1 = eval(equationOut1)
    turtleWindow.goto(10, equationOut1 * 10)
    turtleWindow.pendown()
    for x in range(-9, 10):
        equationOut = equationIn.replace("x", "*" + str(x))
        equationOut = eval(equationOut)
        print("old", str(x*10))
        print("scaled",str(x) )
        turtleWindow.goto(x *10, equationOut * 10)




