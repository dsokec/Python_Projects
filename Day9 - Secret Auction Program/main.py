# TOOLS
# https://thonny.org/
# https://pythontutor.com/visualize.html

from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}

biddingFinished = False

# Python Tutor Code - Visualizer

def findHighestBidder(biddingRecord):
  highestBid = 0
  winner = ""
  # biddingRecord {"Dino": 159, "Matej": 189}
  for bidder in biddingRecord:
    bidAmount = biddingRecord[bidder]
    if bidAmount > highestBid:
      highestBid = bidAmount
      winner = bidder
  clear()
  print(f"The winner is {winner} with a bid of ${highestBid}")

while not biddingFinished:
  name = input("What is your name?: ")
  price = int(input("What is your bid? $"))
  bids[name] = price

  # Provjera unosa
  while True:
    shouldContinue = input("\nAre there any other bidders?\nType 'yes' or 'no'. ")
    if shouldContinue == "no":
      biddingFinished = True
      findHighestBidder(bids)
      break
    elif shouldContinue == "yes":
      clear()
      break
    else:
      print("\nPlease type a correct keyword!")
      continue
      
    