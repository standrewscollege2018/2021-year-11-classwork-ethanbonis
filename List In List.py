people = [["Dr Evil", 45], ["Gru", 34], ["Emperor", 200]]
print(people[0])


person=[]
my_name = input("Name?")
age = input("AGE")
person.append(my_name)
person.append(age)
people.append(person)
for i in range(len(people)):
    print("{} is {} years old".format(people[i][0], people[i][1]))
