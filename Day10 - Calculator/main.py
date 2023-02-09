# Calculator
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# -----------
# Dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
from art import logo
def calculator():
  print(logo)

  # možemo koristit brojeve s decimalnim mjestima
  while True:
    try:
      num1 = float(input("What is the first number?: "))
      break
    except ValueError:
      print("Please type a number value. Thank you!")
      continue

  # A flag
  shouldContinue = True
  while shouldContinue:
    from replit import clear
    
    
    for symbol in operations:
      print(symbol)

    while True:
      operationSymbol = input("Pick an operation from the line above: ")
      if operationSymbol not in operations:
        print("Please type '+', '-', '*', or '/'")
        continue
      else:
        break

    while True:
      try:
        num2 = float(input("\nWhat is the second number?: "))
        break
      except ValueError:
        print("Please type a number value. Thank you!")
        continue
        
    # A hold function
    # https://pythontutor.com/visualize.html#mode=edit
    calculationFunction = operations[operationSymbol]
    answer = calculationFunction(num1, num2)
    
    print(f"\n{num1} {operationSymbol} {num2} = {answer}")

    # Provjera unosa
    while True:
      choice = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
      #if choice is not ["y", "n"]: - ne radi!
      if choice == "y" or choice == "n":
        break
      else:
        print("Please type 'y' or 'n'  Thank you!")
        continue
        
    if choice == "y":
      num1 = answer
      clear()
    else:
      # Changing flag to False
      shouldContinue = False
      # This is a recursion
      # Everything is on reset
      clear()
      calculator()

# Ovo se poziva po pokretanju programa
calculator()