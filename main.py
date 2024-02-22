import random

import colorgram
from turtle import Turtle,Screen

colours = colorgram.extract('image.jpg',30)
RGB=[]
for colour in colours:

    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)
    RGB.append(new_colour)
#print(RGB)

zain_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)
zain_the_turtle.penup()


zain_the_turtle.shape("arrow")
start_value=-200
end_value=start_value+500
step=50
k=1
for i in range(start_value,end_value,step):
    for j in range (start_value,end_value,step):
        zain_the_turtle.goto(j,i)

        zain_the_turtle.dot(10,random.choice(RGB))

    
screen.exitonclick()