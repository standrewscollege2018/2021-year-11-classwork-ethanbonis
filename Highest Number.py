# Number thingymagiggy

word_not = True

while word_not == True:

    try:

        number_1 = int(input("Gimme a number"))

        number_2 = int(input("Gimme another number please"))

        if number_1 < number_2:

            print("Highest number is", number_2)
        elif number_2 < number_1:

            print("Highest number is", number_1)
        else:
            print("Woah no way you were actually so dumb to put the same number in you dumbo.")
    except:
        print("(Slams Uno Reverse Down On Table)")
