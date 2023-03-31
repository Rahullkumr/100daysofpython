'''
HURDLE 2
--------------
The video is from
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
----------------------------------------------------------------------
Hurdle 1 Hints:
    Here there are only two functions available
    	1. turn_left()
    	2. move()
    using these two functions write a function for jumping 
    and also for turning right

    using these 4 functions make the robot reach its destination.
------------------------------------------------------------------------

In hurdle 2, the flag(destination) is set randomly each time 
the play button is pressed.
using the hurdle 1 hints along with an extra condition, 
ie at_goal(), complete the hurdle 2 using while loop
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
while at_goal() != True:
    move()
    jump()