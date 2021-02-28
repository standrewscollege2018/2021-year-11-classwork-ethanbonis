#This is a guessing game where the code will pick a random number and will ask the user if they can guess it.

import random
try_again = True

while try_again == True:

        number_guessed = random.randint(1,100)
        print(number_guessed)
        keep_asking = True
        counter = 0
        while keep_asking == True:

            random_number = int(input("Pick a number between 1 and 100 "))
            counter += 1
            if random_number == number_guessed:

                print("that's right. Number of times guessed:", counter)
                keep_asking = False
            elif random_number < number_guessed:
                print("Higher ")
            else:
                print("Lower ")
        again = input("Do you want to play again? y/n  ")
        if again == "n":
            try_again = False
print("Thanks for playing")





