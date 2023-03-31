'''
HURDLE 4
--------------
The video is from
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

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
-------------------------------------------------------------------------
Hurdle 3 hints:
    The position of walls are set randomly whenever play button is pressed.
    Using hurdle1 and hurdle2 data along with two new methods namely
    wall_in_front() and front_is_clear(), help the robocar reach the flag
--------------------------------------------------------------------------   
Hurdle 4 hints:
    The position, the height and the number of hurdles changes each time 
    this world is reloaded.
    combine data of all previous hurdles and help the robocar reach the flag
''' 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()