import random
from secrets import choice
shuffled=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(shuffled)
cap=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
myKey=[]
for i in range(len(shuffled)):
    myKey.append(cap.index(shuffled[i])-i)
print(shuffled)
print(cap)
print(myKey)
    