#Python file used to test te read/write procedure in python
import random
import string
#creat a string of 10 characters
def getRandomText():
    return ''.join(random.choices(string.ascii_letters, k=10))
#write procedure
with open('file.txt', 'a+') as f:
    for i in range(100):
        f.write(getRandomText()+"\n")
#read procedure and display on console only the strings that contain the 'M' character
with open('file.txt','r') as f:
    listOfLines=f.readlines()
    for i in listOfLines:
        if 'M' in i:
            print(i.replace("\n",""))
        else:
            continue

