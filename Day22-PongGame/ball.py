from turtle import Turtle

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_speed = 0.1
	
	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):		# bounce from top and bottom WALL
		self.y_move *= -1	# changes direction of ball mvmt

	def bounce_x(self):		# bounce from l_paddle and r_paddle
		self.x_move *= -1	# changes direction of ball mvmt 
		self.move_speed *= 0.9

	def reset_position(self):
		self.goto(0, 0)
		self.move_speed = 0.1
		self.bounce_x()		# will change the direction of ball mvmt