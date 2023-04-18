# Move the turtle based on the button pressed

# w = move forward, s = move backward
# a = turn left, d = turn right
# c = clear the screen for new drawing


from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.color("green")

def move_forward():
    t.fd(10)


def move_backward():
    t.back(10)


def reset_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="c", fun=reset_screen)
s.exitonclick()
