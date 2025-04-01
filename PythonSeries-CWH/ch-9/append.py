# adding at the end of the file.
str = "hey! this is the appended text"
f = open("file3.txt", "a")
f.write(str)
f.close()

# note : the no. of time we run this program the str will get appended that no. of times.