# This is a quiz wow
ask_name = True
while ask_name == True:
    name = input("Whats your name ")
    if name.replace(" ", "") == "":
        print("input a real name ")
    else:
        ask_name = False
        print("ok then", name)
questions_theory = True
while questions_theory == True:
    input(int("How many questions do you think you will get right?")


