from turtle import Turtle,Screen
import random

t = Turtle()
s = Screen()

t.penup()
t.left(90)
t.fd(100)
t.pendown()
t.right(90)
t.speed(2)
s.bgcolor("black")

# Draw a triangle, square, pentagon, hexagon, heptagon, 
# octagon, nonagon and decagon sequentially with different colors
colors = [
			"red","green","cyan","maroon",
			"lime","magenta","white",
		  	"violet","orange","violet","indigo"
		]

def draw_shape(no_of_sides):
	angle = 360 / no_of_sides
	for _ in range(no_of_sides):
		t.fd(100)
		t.right(angle)

for shape_sides in range(3,11):
	t.color(random.choice(colors))
	draw_shape(shape_sides)
