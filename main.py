import turtle as t
from turtle import Turtle, Screen
from random import randint

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.color("VioletRed4")

# 360 / num_angle = angle

num = 3
while num < 11:
    tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    angle = 360 / num
    for _ in range(num):
        tim.forward(100)
        tim.right(angle)
    num += 1


# # teacher's solution
#
# import turtle as t
#
# tim = t.Turtle()
#
#










screen = Screen()
screen.exitonclick()
