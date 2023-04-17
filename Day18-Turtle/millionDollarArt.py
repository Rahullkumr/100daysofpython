from turtle import Turtle, Screen
import random

rgb_colors_from_image = [
    (246, 166, 151), (249, 7, 47), (237, 165, 191), (167, 3, 2),
    (183, 7, 34), (24, 95, 186), (206, 78, 150), (223, 162, 78),
    (106, 163, 225), (171, 93, 47), (222, 114, 169), (206, 173, 24),
    (234, 222, 71), (42, 179, 90), (7, 55, 159), (185, 47, 85),
    (101, 87, 198), (238, 70, 29), (114, 222, 207), (5, 107, 81),
    (18, 125, 83), (4, 38, 96), (14, 71, 4), (113, 3, 56),
    (167, 183, 224), (123, 192, 163)
]

t = Turtle()
s = Screen()
s.colormode(255)
t.speed("fastest")
t.penup()           # so that no line is visible
t.hideturtle()

# make the turtle start at lower left position
t.setheading(225)
t.fd(300)
t.setheading(0)     # set turtle face to default ie EAST facing

no_of_dots = 100
for eachdot in range(1, no_of_dots+1):
    t.dot(20, random.choice(rgb_colors_from_image))
    t.fd(50)
    if eachdot % 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)
s.exitonclick()
