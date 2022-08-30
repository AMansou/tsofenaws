import json
def save(key,filename):
    if key=={}:
        print("Please use either the \"load\" or \"newkey\" command before saving")
        return
    with open(filename+".json", "w") as outfile:
        key["saved"]=filename+".json"
        json.dump(key, outfile)
        print(key["name"]+" was saved to " + filename + ".json successfully.")
        return key
def load(filename):
    try:
        with open(filename+".json", "r") as infile:
            key=json.load(infile)
    except FileNotFoundError:
        msg = "Sorry, the file "+ filename + ".json does not exist."
        print(msg) # Sorry, the file John.txt does not exist.
        return {}
    print(key["name"]+" Was loaded from " + filename + ".json")
    return key
