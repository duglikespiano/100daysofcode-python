print('''
   ___________
   \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\\
 .-------------.
/_______________\\
''')


bidders = []


def participate_bid():
    name = input("What is bidder's name?: ")
    price = float(input("What is bid price?: $"))

    bid_info = {
        "name": name,
        "price": price
    }
    bidders.append(bid_info)


keep_going = True
participate_bid()

while (keep_going):
    anyone_else = input("Are there any other bidders? Type 'yes or 'no'. \n")
    if (anyone_else == 'yes'):
        participate_bid()

    else:
        highest_bidder_name = []
        highest_bid_price = 0
        for bidder in bidders:
            if highest_bid_price < bidder["price"]:
                highest_bid_price = bidder["price"]

        for bidder in bidders:
            if highest_bid_price == bidder["price"]:
                highest_bidder_name.append(bidder["name"])

        if len(highest_bidder_name) > 1:
            print(
                "\nThere are more than a person who bid the highest price\nLet the game begin again")
            participate_bid()

        else:
            keep_going = False
        print(
            f'The winner is {highest_bidder_name[0]} with a bid of ${highest_bid_price}')
