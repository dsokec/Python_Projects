# Version 3 _ Format - two decimals place - show number zero
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

perPerson = bill / people
perPersonPercentage = perPerson * (1 + percentage/100)
per = round(perPersonPercentage, 2)

# Google it
# It shows a number zero after the number when it is not neccessary
per = "{:.2f}".format(perPersonPercentage)


print(f"Each person should pay: $", per)
