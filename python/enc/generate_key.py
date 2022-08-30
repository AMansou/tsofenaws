import random
from string import ascii_lowercase
from string import ascii_uppercase
def generateKey(name):
    cap=list(ascii_lowercase)
    encKey=list(ascii_lowercase)
    random.shuffle(encKey)
    decKey=[0]*26
    for i in range(26):
        decKey[ord(encKey[i])-97]=cap[i]
    key={"name" : name, "enckey" : encKey , "deckey" : decKey }
    print("A new key called "+ name +" was created")
    return key
