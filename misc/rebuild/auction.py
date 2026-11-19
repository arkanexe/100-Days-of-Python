bids = {}
should_continue = False
highest_bid = 0
highest_bidder = ""
while not should_continue:
    try:
        name = input("What is your name? ")
        price = int(input("What is your bid? "))
        bids[name] = price
        should_continue = input("Are there other bidders? Type 'yes' or 'no': ").lower() == "no"

        if should_continue:
            for name, bid in bids.items():
                if bid > highest_bid:
                    highest_bid = bid
                    highest_bidder = name
            print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
    except ValueError:
        print("Enter valid details")
