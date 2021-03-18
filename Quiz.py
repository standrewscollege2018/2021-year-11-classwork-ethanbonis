jm,# This is a quiz wow
A = 6
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
    if questions_right <=A:
    print("A")
    except:
        print("Answer needs to be a number ")
    else:
        print("ok")
questions_1 = True
while questions_1 == True:
    try:
        first_question = int(input("How many states are there in America "))
        first_question = False
    except:
        print("Answer needs to be a number ")
    else:
        print("ok")

