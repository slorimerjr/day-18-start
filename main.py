import turtle as t
from turtle import Turtle, Screen
import random
from random import randint



# my shape draw w/ random color solutions

# t.colormode(255)
# tim = t.Turtle()
# tim.pensize(5)


# 360 / num_angle = angle

# num = 3
# while num < 11:
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     angle = 360 / num
#     for _ in range(num):
#         tim.forward(100)
#         tim.right(angle)
#     num += 1


# # teacher's solution
#
# import turtle as t
# from turtle import Screen
# import random
#
# tim = t.Turtle()
#
# num_sides = 5
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
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

# my random walk solution

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# tim.speed(10)
# tim.pensize(10)
#
# for _ in range(100):
#     tim.color(random.choice(colors))
#     tim.left(random.choice(directions))
#     tim.forward(25)
#


# teacher's random walk solution
tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick()