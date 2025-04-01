# to get the line we will each line one by one

with open("mine.log", "r") as f:
    lines  = f.readlines()

lineno = 1  
for line in lines:
    if("python" in line):
        print(f"python is present in line no. {lineno}")
        break
    lineno+=1
   
else: 
    print("python is not present.")