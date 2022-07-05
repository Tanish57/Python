# import turtle
#
# timmy = turtle.Turtle()
import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# # using methods associated with the object
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)     # Object attribute
# my_screen.exitonclick()     # Object method

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
