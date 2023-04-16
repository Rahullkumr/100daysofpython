from turtle import Turtle,Screen
import random
s = Screen()
s.bgcolor("black")

t = Turtle()
t.speed(2)
t.color("green")



# challenge5: Random Walk with random RGB colors

# in order to use RGB colors first change screen color mode
s.colormode(255)

angle = [0,90,180,270]
t.pensize(15)
t.speed("fastest")
def random_color():
	r = random.randint(1, 255)
	g = random.randint(1, 255)
	b = random.randint(1, 255)
	color = (r, g, b)
	return color


for _ in range(200):
	t.color(random_color())
	t.setheading(random.choice(angle))
	t.fd(30)