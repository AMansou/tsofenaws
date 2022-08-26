import os
f = open("Alice.txt", "r",encoding='utf-8-sig')
alice=f.read().split()
if alice==[]:
    print("There's not much there :(")
    exit()
max=alice[0].lower()
dict={}
for i in alice:
    if i in ".,:;\'\"!?":
        continue
    word=i.lower()
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
        # print(dict)
    if dict[word]>dict[max]:
        max=word
print("The word with the most occurences is:")
print(max,":",dict[max])
# print(dict)
