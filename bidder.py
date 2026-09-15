
bids = {}
isBidding = True

while isBidding:
    name = input("What is your name? ").lower()
    bidding_price = int(input("What is your bidding price? "))

    bids[name] = bidding_price

    questions = input("Are there any other bidders? Type 'yes' or 'no' .")

    if questions == 'no':
        isBidding = False
        final_bid = 0
        highest_bidder = " "
        for auction in bids:
            bid = bids[auction]

            if bid > final_bid:
                final_bid = bid
                highest_bidder = auction
        print(f"The winner is {highest_bidder} with a bid of ${final_bid}")
