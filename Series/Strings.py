name = "apple"

nameShort = name[0:3]
print(len(name))

print(nameShort)


print(name[:4]) # is same as print(name[0:4]) , 0 is the start

print(name[1:]) # is same as print(name[1:5]) , 5 is the length

print(name.count("p"))

print(name.endswith("ple"))
print(name.startswith("App"))
capitalName = name.capitalize()
print(capitalName)

name2 = "Hello World!"
result = name2.find("World")
print(result)


a= "apple is the best\
company in the world. \
It has more valuation in the world. "
print(a)

