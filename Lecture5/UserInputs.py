# Getting inputs from user by input() method
yourName = input("What is your name? : \n")
print("Your name is : " + yourName)

# random liabrary and choice method
import random
valu = random.choice("123")
print(valu)

# Enums 
from enum import Enum
class values(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3 

valu = int(valu)
print(values(valu))