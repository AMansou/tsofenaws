def encdecrypt(inFile,key,outFile,command): #Encrypts/Decrypts (based on the key provided) an inFile into outFile
    try:
        with open(inFile) as f_obj:
            plaintext = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file "+ inFile + " does not exist."
        print(msg)
        return
    ciphertext=substitute(plaintext.lower(),key)
    with open(outFile, 'w') as file_object:
        file_object.write(ciphertext)
    print(inFile+ " Was " + command + "rypted to " + outFile)

def substitute (plaintext,key): #helper function to perform the substitution
    return "".join([key[ord(x)-97] if x.isalpha() else x for x in plaintext ])
