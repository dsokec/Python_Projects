# ASCII art
# https://ascii.co.uk/art
print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# Game over
gameOver = "\nGame Over."
hole = "\nFall into a hole."
trout = "\nAttacked by trout."
beasts = "\nEaten by beasts."
fire = "\nBurned by fire."
# Win
win = "\nYou Win."

#Apostrophe usage \'
direction = input('"\nYou\'re at CrossRoads, where do you want to go ? Type "Left" or "Right."\n> ')
# direction = input("You\'re at CrossRoads, where do you want to go ? Left or right? Type L or R >> ").lower()

# Lowercase letter
direction = direction.lower()

# 1a Direction Left
if direction == "left":
  mode = input('"\nYou\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across."\n> ')
  mode = mode.lower()

  # 1a-1a Wait
  if mode == "wait":
    color = input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n> ")
    color = color.lower()
    
    # 1a-1a-1a Win
    if color == "yellow":
      print(win)

    # 1a-1a-1b Fire
    elif color == "red":
      print(fire + gameOver)

    # 1a-1a-1c Beasts
    elif color == "blue":
      print(beasts + gameOver)

    # 1a-1a-1d Game over
    else:
      print(gameOver)
      
  # 1a-1b Swim
  else:
    print(trout + gameOver)

# 1b Direction Right
else:
  print(hole + gameOver)

