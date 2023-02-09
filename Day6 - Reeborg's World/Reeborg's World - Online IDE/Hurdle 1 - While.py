def turn_right():
    turn_left()
    turn_left()
    turn_left()

def preskoci_zid():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
numberOfHurdles = 6
# while something_is_true:
while numberOfHurdles > 0:
    preskoci_zid()
    numberOfHurdles -= 1
    print(numberOfHurdles)