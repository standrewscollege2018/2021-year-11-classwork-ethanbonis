#This program will take an exam mark and give an exam result

A = 90
B = 80
C = 69
F = 50



result = int(input("What was your exam mark?"))

if result <=F:
    print("Fail")

elif result <=C:
    print("C")

elif result <=B:
    print("B")

elif result <=A:
    print("A")

elif result <=1000:
    print("A+")

elif result <=10000:
    print("A++")

elif result <=100000:
    print("A+++")

else:
    print("Invalid Mark")

