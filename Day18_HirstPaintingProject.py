from turtle import Turtle, Screen
import random

#working with berry the turtle
berry = Turtle()
berry.hideturtle()

myscreen = Screen()
myscreen.colormode(255)  #colour r,g,b values can range from 0 to 255

# import colorgram
# colorgram_list = colorgram.extract("image.jpg", 30)
# color_list = []
# for item in colorgram_list:
#     rgb_value = tuple(item.rgb)
#     color_list.append(rgb_value)
#after running this code we get this as the final rgb values of the colours(excluding background colours)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

berry.speed("fastest")
berry.penup()  #don't need pendown to make dots
berry.teleport(-250,-250)  #goes to bottom left corner without drawing line
for y in range(10):
    for x in range(10):
        berry.dot(20, random.choice(color_list))
        berry.forward(50)
    berry.left(90)
    berry.forward(50)
    berry.left(90)
    berry.forward(500)
    berry.left(180)

myscreen.exitonclick()  #screen is diplayed till it is clicked upon
