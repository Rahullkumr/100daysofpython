from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		# Creating paddle
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)	
		# each square = 20X20, 20x5 = 100 and 20x1 = 20  ==> paddle(height=100, width=20)
		self.penup()
		self.goto(position)

	def go_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)