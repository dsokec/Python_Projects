def turn_right():
    turn_left()
    turn_left()
    turn_left()

def preskoci_zid():
    turn_left()
    # move() - ovo nije ispravna linija koda - radi, ali ne tako
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    # move() - ovo nije ispravna linija koda - radi, ali ne tako
    while front_is_clear() == True:
        move()
    turn_left()


while not at_goal():
    if wall_in_front() == True:
        preskoci_zid()
    else:
        move()