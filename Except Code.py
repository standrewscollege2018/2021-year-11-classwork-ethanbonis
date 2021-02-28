
keep_asking = True

while keep_asking == True:

    try:
        number = int(input("enter integer"))
        print("You chose", number)
        keep_asking = False
    except:
        print("Thats not an integer")

print("All Done")
