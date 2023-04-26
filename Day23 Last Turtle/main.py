from turtle import Turtle, Screen
from ground import Ground
from ball import Ball
from time import sleep


s = Screen()
s.tracer(0)
s.setup(height=600, width=600)
s.bgcolor("black")
s.title("Bouncing Ball")

ground = Ground()
ball = Ball()


while True:
    s.update()
    ball.fall()

    if ball.ycor() < -220:
        ball.change_mvmt_dir()
        ground.change_color()

    # change direction of ball movement
    if ball.ycor() > 400:
        ball.change_mvmt_dir()




s.exitonclick()
