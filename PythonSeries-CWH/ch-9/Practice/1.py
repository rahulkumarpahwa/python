with open("./poem.txt") as f :
    if "twinkle" in f.read():
        print(True)
    else:
        print(False)