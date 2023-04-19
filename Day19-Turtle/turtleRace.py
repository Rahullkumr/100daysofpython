from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)
s.title("Turtle Race")
s.bgcolor("black")

colors = ["green", "yellow", "white", "magenta", "orange", "red"]
y_positions = [-120, -70, -20, 30, 80, 130]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[turtle_index])
	new_turtle.goto(x=-230, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)

user_bet = s.textinput(title="Turtle Race",
                       prompt="Which turtle will u bet on? ")

if user_bet:
	is_race_on = True


while is_race_on:
	for turtles in all_turtles:
		if turtles.xcor() > 230:
			is_race_on = False
			winning_color = turtles.pencolor()
			if winning_color == user_bet:
				print(f"\nYou've won. The {winning_color} turtle is the winner")
			else:
				print(f"\nYou've lost. The {winning_color} turtle is the winner")

		
		random_distance = random.randint(1,10)
		turtles.fd(random_distance)


s.exitonclick()
