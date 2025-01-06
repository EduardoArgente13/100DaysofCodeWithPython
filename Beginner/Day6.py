#Maze Solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def path_to_follow():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    path_to_follow()
