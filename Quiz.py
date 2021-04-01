# This is a quiz wow
score = 0
question_list = ["How many states are there in the U.S", "What is the capital of malasia", "Are you a cool person", "Rudolph had a red what", "Who plays the most recent Spider Man", "What colour is grass"]
answer_list = ["50", "Kuala Lumpur", "yes", "no", "Tom Holland", "green"]
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
        if questions_right >A:
            print("I mean there's only 6 question but ya know, aim high")
    except:
                print("Answer needs to be a number ")
    else:
                print("ok")
for i in range(len(question_list)):
    print("{}".format(question_list[i]))
    answer = input()
    if answer == answer_list[i]:
        print("yes")
        score += 1

    else:
        print("no")

if answer == answer_list[5]:
    print("final score is", score)
else:
    print("Final score is", score)

