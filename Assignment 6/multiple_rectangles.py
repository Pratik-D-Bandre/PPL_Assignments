import turtle
pen = turtle.Turtle()
pen.width(10)
pen.color("green")

def rectangle():
    pen.forward(200)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(100)

rectangle()
pen.color("white")
pen.forward(50)
pen.color("green")
rectangle()
