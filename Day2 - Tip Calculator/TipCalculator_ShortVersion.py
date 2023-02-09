# Version 1
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

billPerson = float(bill) / int(people)
tipPerson = round(billPerson * (1 + float(int(percentage)/100)), 2)
print(f"Each person should pay: ${tipPerson}")