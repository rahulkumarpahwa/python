for i in range(1, 21):
    print(i)
    
# here we mention the range to print the numbers in the range.

###############################
# we can add the steps/jumps in loop as well

for i in range(0, 101, 4): # start, end. jumps
    print(i) # will print at the step of 4
    
# note : in the range always increase it by 1.

############
# we can iterate over the tuple, list and strings as well.

# lists
l = [1,2,3,4,5,6]
for i in l:
    print(i)
    
print("#######################")

# tuple 
t = {1,2,3,4,5,6}
for i in t:
    print(i)
    
print("######################")

# strings : with each letter to be get printed

str = "Apple is the best"
for i in str:
    print(i)
    
#################################################

print("for loop with else")
# it will print the else case when loop will be finished.

for i in range(1, 10):
    print(i)
else:
    print("done")
    
# here done will be printed when loop get finished.

##################################################
print("##################################")
print("break keyword")

for i in range(100): # here i will be auto initialized to 0
    if i == 34:
        break # exit the loop when i = 34
    print(i)
    
print("##################################")
print("Continue")

for j in range(100): # here j will be auto initialized to 0
    if (j == 34):
        continue # means skip the iteration no. 34
    print(j)
    
print("##################################")
print("pass statement")
# pass statement  
# when we want to do nothing.

for i in range(0, 100):
    pass  # without the pass here, program will throw error.
print("here nothing will print")
