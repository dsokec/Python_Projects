# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

def idi_do_cilja():
    preskoci_zid()
    preskoci_zid()
    preskoci_zid()
    preskoci_zid()
    preskoci_zid()
    preskoci_zid()

# Pozovem rad samo jedne funkcije 'idi_do_cilja()'
idi_do_cilja()