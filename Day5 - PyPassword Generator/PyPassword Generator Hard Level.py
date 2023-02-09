#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordList = []

# e.g. nr_letters = 4
for znak in range(1, nr_letters + 1):
  passwordList.append(random.choice(letters))
  
  # 1 - 4
  # randomZnak = random.choice(letters)
  # password += randomZnak

for znak in range(1, nr_symbols + 1):
  passwordList.append(random.choice(symbols))

for znak in range(1, nr_numbers + 1):
  passwordList.append(random.choice(numbers))

# polje znakova odvojeni ' '
# print(passwordList)


# funkcija Shuffle je za polje
# Potreban je modul random
random.shuffle(passwordList)
# print(passwordList)

# jedan string
password = ""
for znak in passwordList:
  password += znak

print(f"Vasa lozinka je: {password}")
