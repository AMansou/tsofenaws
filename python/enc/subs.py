from encdec import encdecrypt
from generate_key import generateKey
from saveload import save,load
from info import info
from help import help
from intro import intro

def checkError(command, length, msg):
    if len(command) != length:
        print(msg)
        return True

def cli():
    intro()
    key={}
    while True:
        inp=input("subs>")
        command=inp.split()
        if len(command) < 1 :
            continue
        ########################################################################
        if command[0] == "newkey" and not checkError(command,2,"Usage: newkey <key name of your choice>"):
                name=command[1]
                key=generateKey(name)
        ########################################################################
        elif (command[0] == "enc" or command[0] == "dec") and not checkError(command,3,"Usage: " +command[0]+" <input file> <output file>"):
            if key == {}:
                print("Please use either the \"load\" or \"newkey\" command before encrypting/decrypting")
            else:
                inFile=command[1]
                outFile=command[2]
                encdecrypt(inFile,key[command[0]+"key"],outFile,command[0])
        ########################################################################
        elif command[0] == "save" and not checkError(command,2,"Usage: save <filename>"):
                filename=command[1]
                key=save(key,filename)
        ########################################################################
        elif command[0] == "load" and not checkError(command,2,"Usage: load <filename>"):
                filename=command[1]
                key=load(filename)
        ########################################################################
        elif command[0] == "info":
            info(key)
        ########################################################################
        elif command[0] == "help":
            help()
        ########################################################################
        elif command[0] == "done":
            print("Exiting...")
            exit()
        ########################################################################
        else:
            print("Please enter a valid command! Enter \"help\" for a list of valid commands.")

################################################################################
                                                                               #
cli()                                                                          #
                                                                               #
################################################################################
