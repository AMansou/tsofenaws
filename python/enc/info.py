from string import ascii_lowercase
from string import ascii_uppercase
def info(key):
    if key == {}:
        print("You need to load/create a key first.")
        return
    print("Current key:\t" + key["name"])
    if "saved" in key.keys():
        print("State:\t\tSaved in " + key["saved"])
    else:
        print("State:\t\tNot saved")
    print("Encryption:\n\t"+ascii_lowercase+"\n\t"+"".join(key["enckey"]))
    print("Decryption:\n\t"+ascii_lowercase+"\n\t"+"".join(key["deckey"]))
