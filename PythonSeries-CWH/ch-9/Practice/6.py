with open("mine.log", "r") as f:
    if "python" in f.read():
        print(True)
    else:
        print(False)