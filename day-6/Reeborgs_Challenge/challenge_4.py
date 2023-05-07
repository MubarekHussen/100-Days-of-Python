def turn_right():
    turn_left()
    turn_left()
    turn_left()
def up():
    if (not front_is_clear()):
        if (wall_in_front() and not wall_on_right()):
            down()
    if (not front_is_clear()):
        turn_left()
    if (front_is_clear()):
        if (at_goal()):
            return
        move()
def down():
    turn_right()
    move()
    turn_right()
    move()
while (not at_goal()):
    while(front_is_clear()):
        if (at_goal()):
            break
        move()
    while ((wall_on_right() or wall_in_front()) and not at_goal()):
        up()
    if (at_goal()):
        break
    down()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
