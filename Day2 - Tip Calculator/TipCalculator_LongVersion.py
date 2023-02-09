# Version 2 _ Long Version
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

perPerson = float(bill) / int(people)
multiplicationPercentage = 1 + (int(percentage) / 100)

totalPerPerson = round(perPerson * multiplicationPercentage,2)

print(f"Each person should pay: ${totalPerPerson}")