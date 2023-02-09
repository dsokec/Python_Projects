# The Functions
# move()
# turn_left()
  
# The Conditions
# front_is_clear()
# wall_in_front()
# at_goal()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def preskoci_zid_ispred_sebe():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def nastavi_hodati():
    move()

while not at_goal():
    if wall_in_front() == True:
        preskoci_zid_ispred_sebe()
    else:
        nastavi_hodati()