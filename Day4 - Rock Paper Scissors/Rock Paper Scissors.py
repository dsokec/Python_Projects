# https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

gameImages = [rock, paper, scissors]

userChoice = int(input("What do you choose?\nType 0 for Rock, \n1 for Paper or \n2 for Scissors. \n> "))

if userChoice >=3 or userChoice < 0:
  print("\nYou typed an invalid number.\nYou lose.")
else:
  print("\nYou have chosen:\n")
  print(gameImages[userChoice])

  computerChoice = random.randint(0,2)
  print("\nComputer choose: \n")
  print(gameImages[computerChoice])


  if userChoice == 0 and computerChoice == 2:
    print("\nYou Win!")
  elif userChoice == 2 and computerChoice == 0:
    print("\nYou lose.")
  elif computerChoice > userChoice:
    print("\nYou lose.")
  elif userChoice > computerChoice:
    print("\nYou Win!")
  elif computerChoice == userChoice:
    print("\nIt's a draw.")
