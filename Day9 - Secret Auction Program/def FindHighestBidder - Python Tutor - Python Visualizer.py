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
 
bids = {
    "Dino" : 190,
    "Marko" : 299,
    "Franjo" : 999
}

findHighestBidder(bids)