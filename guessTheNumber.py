#Guess the number between an interval choose by user
import random
from textStyle import textStyle

class User:
    lowVal=0
    highVal=0

def getARandomNumber(lowInterval,highInterval):
    return random.randint(lowInterval,highInterval)

user=User()
while True:
    lowInterval = input("Write the left side of the interval: ")
    highInterval = input("Write the right side of the interval: ")
    if lowInterval.isdigit() and highInterval.isdigit():
        user.lowVal=int(lowInterval)
        user.highVal=int(highInterval)
        if user.lowVal<= user.highVal:
            print(textStyle.OKGREEN+"OK"+textStyle.ENDC)
            break
        else:
            print(textStyle.FAIL+"Not OK"+textStyle.ENDC)
            continue
    else:
        print(textStyle.FAIL+"Not OK"+textStyle.ENDC)
        continue
