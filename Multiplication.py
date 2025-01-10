#Diego Osornio
#1/8/2025

import random

def quiz():
    print("welcome to your Quiz")
    Questions = input(" How many Questions do you want?")
    Num1 = random.randint(1,10)
    Num2 = random.randint(1,10)
    score = 0


    for i in range(int(Questions)):
        Num1 = random.randint(1,10)
        Num2 = random.randint(1,10)
        response = (int(input("Whats " + str(Num1) + " X " + str(Num2) + " Equal?" )))
        if response == (Num1 * Num2):
          print("Congrats You got that right!")
          score = score + 1
        else:
            print("you got this wrong")
            print("Your anwser : " + (str(response)))

    print(str  (score) + " out of " + str(Questions))

quiz()

