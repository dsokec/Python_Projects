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

# While loop - kada ne znamo egzaktni broj elemenata
# While loop nema konačan broj. Treba samostalno pronaći
    
# while something_is_true:
# while at_goal() != True:
# while at_goal() == False:
while not at_goal():
    preskoci_zid()
    
# while 5 > 3: - Infinte loop