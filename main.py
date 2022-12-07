
print("First line") #TODO : check this line later

_values = [0]*50
for i in range(0,50):
    _values[i]=i+(i+1)
    print(_values[i])

print("Last line")

for i in range(0,10000):
    if i%2==0:
        print(str(i)+" e par")
    else:
        continue
#just a comment
#some comments to check the commit with a new branch
#another comment
