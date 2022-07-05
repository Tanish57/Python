from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("PaleVioletRed")
tim.pencolor("magenta")

# i = 0
# while i < 4:
#
#     tim.forward(100)
#     tim.right(90)
#     i += 1
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.forward(50)

# j = 0
# for _ in range(15):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pendown()

import heroes
print(heroes.gen())

import random
colors = ["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# tim.color("red")

# for _ in range(5):
#     tim.right(72)
#     tim.forward(100)


screen = Screen()
screen.exitonclick()