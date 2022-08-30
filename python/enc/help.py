def help():
    print("""
    dec <input> <output> - decrypt an input file to the specified output file.
    done - exit program.
    enc <input> <output> - encrypt an input file to the specified output file.
    help - show list of available commands.
    info - Show information about the current key.
    load <filename> - load a key from the given file name.
    newkey <name> - Generate a key and give it a name.
    save <filename> - save current key to the specified file name.
    """)
