name_is = []
bid = []
leader = ""
max_bid = 0

Continue = True
while Continue == True:
    name = input("Name Please   ")
    name_is.append(name)
    bidding_price = int(input("How much are you willing to bid?   "))
    bid.append(bidding_price)
    if bidding_price > max_bid:
        max_bid = bidding_price
        leader = name

    print(name, "Is betting $", bidding_price)

    Again = input("Do you want to enter another bid? y/n  ")
    if Again == "n":
        Continue = False

print("Highest Bidding Price is: ${} made by {}".format(max_bid, leader))
