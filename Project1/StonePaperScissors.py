import sys
import random 
import math
from enum import Enum 

yourInput = input("\n\nEnter Your choice : \n\n 1 -> Rock \n 2 -> Paper \n 3 -> Scissor \n")
yourInput = int(yourInput)

if yourInput > 3 or yourInput < 1 :
    print(" \nYou have chosen a wrong number :( \nTry again!")
    sys.exit()

class choices(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

computerInput = int(random.choice("123"))
yourChoice = str(choices(yourInput)).replace("choices.","")
computerChoice = str(choices(computerInput)).replace("choices.","")

print("\nYou chose : " + yourChoice)
print("Computer chose : " + computerChoice + "\n")

if (computerInput == 2 and yourInput == 3) or (computerInput == 1 and yourInput == 2) or (computerInput == 3 and yourInput == 1):
    print("HURRAY! You won !")
elif computerChoice == yourChoice:
    print("Woah! Its a tie.")
else:
    print("OOPS! You lost!")