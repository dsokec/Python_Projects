# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

# Ucitaj mapu problem_world3.json
# kao i ostale mape 2 i 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# u pitanju je definirana točka na prilagođenoj mapi
# to je samo za pocetak sa ciljem da udari u zid
while front_is_clear() == True:
    move()
turn_left()

# while at_goal() == false:
while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
        