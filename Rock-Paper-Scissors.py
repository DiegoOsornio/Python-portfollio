#Diego Osornio
#1/6/2025
#Initailaize
import random

#Functions


def Rockpapercut():
    print("welcome to Rock Paper Sissors!")
    y = random.randint(1,3)
    player = input("Selection: ")

    if y == 1:
        y = "Paper"
    if  y == 2:
        y= "Rock"
    if  y == 3:
        y = "Scissors"




    if player == "Paper" and y ==  "Scissors":
        print("Computer won")
    if player == "Scissors" and y == "Paper":
        print("Player won")
    if player == "Rock" and y == "Scissors":
        print("Computer won")
    if player == "Scissors" and y == "Rock":
        print("Player won")
    if player  == "Rock" and y  == "Paper":
        print("Player won")
    if player == "Rock" and y  == "Rock":
        print("Computer won")











Rockpapercut()
