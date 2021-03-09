#this code will calculate a fine for people

keep_asking = True
wanted = ["John Smith", "Helga Norman", "Zach Conroy"]
while keep_asking  == True:
    try:
        name = input("Enter Name?: ")
        if name in wanted:
            print("Yo your going to jail ")
            keep_asking = False
        elif name == "":
            print("name ")
        else:
            speed = int(input("speed please?: "))


            if speed <= 10:
               print(name, "you need to pay $30 ")
            elif speed in range(10,20):
                print(name, "you need to pay $80 ")
            elif speed in range(20,30):
                print(name, "you need to pay $130 ")
            else:
                print(name, "you need to pay $180 ")




    except:
        print("INSERT NUMBER ")
