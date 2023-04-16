from turtle import Turtle, Screen
import random

s = Screen()
s.bgcolor("black")

t = Turtle()

# challenge6: Draw a SPIROGRAPHY with different RGB colors

s.colormode(255)
t.speed("fastest")
def random_color():
	r = random.randint(1, 255)
	g = random.randint(1, 255)
	b = random.randint(1, 255)
	color = (r, g, b)
	return color

for _ in range(60):
	t.color(random_color())
	t.circle(100)
	t.left(6)
