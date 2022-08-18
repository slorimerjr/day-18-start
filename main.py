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
# from turtle import Screen
# import random
#
# tim = t.Turtle()
#
# num_sides = 5
# colors = ["LightSteelBlue", "PaleGoldenrod", "Chartreuse", "DeepPink", "AntiqueWhite", "Peru", "Indigo", "DarkGray", "AliceBlue", "DarkSlateGray", "DarkRed"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_sides in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides)









screen = Screen()
screen.exitonclick()
