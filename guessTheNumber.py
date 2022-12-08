#Guess the number between an interval choose by user
import random
from textStyle import textStyle
from time import sleep
#class for interval
class rangeObj: # TODO: Change the name with another one
    lowVal=0
    highVal=0
#generate a random number
def getARandomNumber(lowInterval,highInterval):
    return random.randint(lowInterval,highInterval)
#Main logic for the guess game
rangeObj=rangeObj()
#function to enter the interval numbers
def enterTheNumbers():
    while True:
        lowInterval = input("Write the left side of the interval: ")
        highInterval = input("Write the right side of the interval: ")
        if lowInterval.isdigit() and highInterval.isdigit():
            rangeObj.lowVal=int(lowInterval)
            rangeObj.highVal=int(highInterval)
            if rangeObj.lowVal<=rangeObj.highVal:
                #print(textStyle.OKGREEN+"OK"+textStyle.ENDC)
                if rangeObj.lowVal+10<rangeObj.highVal:
                    return True
                else:
                    print(textStyle.FAIL + textStyle.BOLD+"Not OK ->" + textStyle.ENDC + textStyle.OKCYAN +textStyle.BOLD+ " The second number should be with at least 10 greater than the first one to make the game more enjoyable" + textStyle.ENDC)
                    while True:
                        choice = input(textStyle.OKGREEN +textStyle.BOLD+ "Do you want to add automatically 10 to your second number (option 1) or choose again 2 numbers (option 2) ? (1/2) : " + textStyle.ENDC)
                        if choice == '1' or choice == '2':
                            if choice == '1':
                                rangeObj.highVal = rangeObj.lowVal + 10
                                return True
                            else:
                                break
                        else:
                            secondTry=input(textStyle.FAIL +textStyle.BOLD+ "You must to write 1 or 2. Do you want to retry or exit? (retry/exit) : " + textStyle.ENDC)
                            if secondTry == "retry":
                                continue
                            elif secondTry == "exit":
                                break
                            else:
                                return False
            else:
                print(textStyle.FAIL+textStyle.BOLD+"Not OK ->"+textStyle.ENDC+textStyle.OKCYAN+textStyle.BOLD+" The first number must to be greater then the second one"+textStyle.ENDC)
                continue
        else:
            print(textStyle.FAIL+textStyle.BOLD+"Not OK - >"+textStyle.ENDC+textStyle.OKCYAN+textStyle.BOLD+" Those inputs must to be numbers"+textStyle.ENDC)
            continue
#game logic part
def loadTheGame():
    notGuess=True
    randomNumber=getARandomNumber(rangeObj.lowVal, rangeObj.highVal)
    while notGuess:
        userAnswer=input(textStyle.BOLD+textStyle.OKGREEN+"Enter your guess: "+textStyle.ENDC)
        if userAnswer.isdigit():
            answer=int(userAnswer)
            if answer==randomNumber:
                print(textStyle.OKGREEN+textStyle.BOLD+ "Congrats, you guess the number and "+textStyle.ENDC+textStyle.OKBLUE+textStyle.BOLD+"WON"+textStyle.ENDC+textStyle.OKGREEN+textStyle.BOLD+" the game" + textStyle.ENDC)
                notGuess=False
            elif answer<randomNumber:
                print(textStyle.OKBLUE + textStyle.BOLD + "You did not guess the number, the number is greater than your choice: " + textStyle.ENDC + textStyle.OKGREEN + textStyle.BOLD + str(answer) + textStyle.ENDC)
            elif answer>randomNumber:
                print(textStyle.OKBLUE + textStyle.BOLD + "You did not guess the number, the number is lower than your choice: " + textStyle.ENDC + textStyle.OKGREEN + textStyle.BOLD + str(answer) + textStyle.ENDC)
        else:
            print(textStyle.FAIL+textStyle.BOLD+"Please enter a valid number between the interval displayed above!"+textStyle.ENDC)
            continue
    print(textStyle.WARNING + textStyle.BOLD+"Thanks for playing the game, have a nice day." + textStyle.ENDC)
#execute the functions to play the game
def playTheGame():
    isOk=False
    isOk=enterTheNumbers()
    if isOk:
        print(textStyle.OKGREEN+textStyle.BOLD+"OK - >"+textStyle.ENDC+textStyle.OKCYAN+textStyle.BOLD+" The game will start soon"+textStyle.ENDC)
        for i in range(0,50):
            sleep(0.05)
            print(textStyle.BOLD+textStyle.OKBLUE+".", end = '')
        print("\n"+textStyle.OKGREEN+textStyle.BOLD+"Guess the number between your interval "+textStyle.ENDC+textStyle.OKCYAN+textStyle.BOLD+"[ "+str(rangeObj.lowVal)+" , "+str(rangeObj.highVal)+" ]"+textStyle.ENDC)
        loadTheGame()
    else:
        print(textStyle.FAIL +textStyle.BOLD+ "Not OK ->" + textStyle.ENDC + textStyle.OKCYAN +textStyle.BOLD+ " The game could not start, something went wrong" + textStyle.ENDC)
#Run the game
playTheGame()