import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("PaleVioletRed")
tim.pencolor("DarkOrchid")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r,g,b)
    return rgb

tim.speed("fastest")
tim.width(15)
import random
# colors = ["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()