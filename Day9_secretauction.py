print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `'-------'`
                       .-------------.
                      |_______________|
''')
print("Welcome to the secret auction program!")
auction = {}

def find_highest_bidder(auction):
    bidvalues = list(auction.keys())
    highest_bid = max(bidvalues)
    highest_bidder = auction.get(highest_bid)
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}! Congratulations!")

while True:
    name = str(input("What is your name?\n"))
    try:
        bid = int(input("What's your bid?\n$"))
        if bid<=0:
            print("Please enter a valid bid.")
            continue
        if bid in auction:
            print(f"A bid of ${bid} has already been made! Please enter another bid.")
            continue
    except:
        print("Please enter a valid bid.")
        continue
    auction[bid] = name
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if add_bidders != "yes":
        print("\n"*100)  #to clear screen
        find_highest_bidder(auction)
        break
    else:
        print("\n"*100)

