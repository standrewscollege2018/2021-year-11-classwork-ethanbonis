# This is a quiz wow
A = 6
B = "Thats Correct"
C = "Thats Incorrect"
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
    try:
        print("How many questions do you")
        questions_right = int(input("think you will get right? "))
        questions_theory = False
        if questions_right >A:
            print("I mean there's only 6 question but ya know, aim high")
    except:
                print("Answer needs to be a number ")
    else:
                print("ok")
questions_1 = True
while questions_1 == True:
    try:

