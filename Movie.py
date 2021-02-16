#This program tell the user the price of a movie ticket based on their age

eighteen = 12
thirteen = 9
five_plus = 7
under_five = 5


#Program asks for age
result = int(input("What age are you?"))

#Program tells user the price

if result >=eighteen:
    print("12")

elif result <=thirteen:
    print("9")

elif result <=five_plus:
    print("7")

elif result <=Under_five:
    print("free")

elif result <=1000:
    print("A+")

elif result <=10000:
    print("A++")

elif result <=100000:
    print("A+++")

else:
    print("Invalid Mark")
