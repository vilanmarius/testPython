# This file is used to create a calculator

# Function to display the text
class textStyle:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def displayMenu():
    print(textStyle.OKBLUE+textStyle.BOLD+"Menu calculator: "+textStyle.ENDC)
    print("1. Adunare")
    print("2. Scadere")
    print("3. Inmultire")
    print("4. Impartire")
    print("5. Puterea")
    print("6. Moldulul")
    print("0. Iesire")

def switch(case, firstInput, secondInput):
    match case:
        case 0: return -99
        case 1: return firstInput+secondInput
        case 2: return firstInput-secondInput
        case 3: return firstInput*secondInput
        case 4: return firstInput/secondInput
        case 5: return pow(firstInput,secondInput)
        case 6: return abs(firstInput)

while(1):
    displayMenu()
    option=int(input(textStyle.BOLD+textStyle.OKCYAN+"Alege optiune: "+textStyle.ENDC))
    if option == 0:
        break
    firstInput=input("Primul numar: ")
    if option != 6:
        secondInput=input("Al doilea numar: ")
    if option == 4:
        if secondInput == "0":
            print("Al doilea numar trebuie sa fie diferit de 0!")
            continue;
    print(textStyle.OKGREEN+textStyle.BOLD+"\nRezultatul este: "+str(switch(option,float(firstInput),float(secondInput)))+"\n"+textStyle.ENDC)
