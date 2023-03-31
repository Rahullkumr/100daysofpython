'''
HURDLE 1
-------------

The video is from
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

Here there are only two functions available
	1. turn_left()
	2. move()
using these two functions write a function for jumping 
and also for turning right

using these 4 functions make the robot reach its destination.
''' 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for x in range(1,7):
    move()
    jump()