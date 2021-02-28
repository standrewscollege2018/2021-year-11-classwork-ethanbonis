import random
import time

raffle_list = []

Continue = True

item = input("What item are we raffling?")

while Continue == True:
    name = input("Name Please   ")
    raffle_list.append(name)
    Again = input("Do you want to enter another name? y/n  ")
    if Again == "n":
        Continue = False
print("Thanks for playing")

time.sleep(2)
print("These are the contestants", raffle_list)
time.sleep(2)
print("And the winner is...")
time.sleep(2)
winner = random.randint(0, len(raffle_list))
time.sleep(2)
print(raffle_list[winner], "who won a", item)
