#link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_left():
    ...
def is_facing_north():
    ...  
def wall_on_right():
    ... 
def wall_in_front():
    ...
def right_is_clear():
    ...
def at_goal():
    ...
def move():
    ...
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def face_north():
    while is_facing_north()==False:
        turn_left()
while at_goal()==False:
    if not wall_on_right() and not wall_in_front():
        face_north()
        move()
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and not wall_in_front():
        move()
    else:
        turn_left() 