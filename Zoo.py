#This code will ask for your age and based on this info, will ask -
#you to pay the child price or to pay the adult price.

CHILD_AGE = 13

age = int(input("What is your age?"))

if age <= CHILD_AGE:
    print("child")
else:

    print("adult")
