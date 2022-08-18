import turtle as t
from turtle import Turtle, Screen
from random import randint

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.color("VioletRed4")

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(3):
    tim.forward(100)
    tim.right(120)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(5):
    tim.forward(100)
    tim.right(72)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(6):
    tim.forward(100)
    tim.right(60)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(7):
    tim.forward(100)
    tim.right(51.43)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(8):
    tim.forward(100)
    tim.right(45)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(9):
    tim.forward(100)
    tim.right(40)

tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(10):
    tim.forward(100)
    tim.right(36)


# teacher solution

































screen = Screen()
screen.exitonclick()
