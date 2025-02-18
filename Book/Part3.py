#strings

str = "apple\'s eye"

print(str)
str = r'apple"s eye' # r stands for raw string.

print(str)
str2 = "mapple"

# only strings can concatenate with +

###################################################################3

# string methods:

# Different categories of string methods are given below.
# Content test functions 
s = "Hello123"
print(s)
print(s.isalpha())      # False, contains numbers
print(s.isdigit())      # False, contains letters
print(s.isalnum())      # True, only letters and numbers
print(s.islower())      # False, contains uppercase letters
print(s.isupper())      # False, contains lowercase letters
print(s.startswith("He"))  # True, starts with "He"
print(s.endswith("123"))   # True, ends with "123"

# Search and replace
print(s.find("lo"))     # 3, position of "lo"
print(s.replace("Hello", "Hi"))  # "Hi123"

# Trim whitespace
s2 = "  Hello  "
print(s2.lstrip())      # "Hello  "
print(s2.rstrip())      # "  Hello"
print(s2.strip())       # "Hello"

# Split and partition
s3 = "apple,banana,grape"
print(s3.split(","))     # ['apple', 'banana', 'grape']
print(s3.partition(",")) # ('apple', ',', 'banana,grape')

# Join
s4 = "Hello"
print("-".join(s4))     # "H-e-l-l-o"

######################################################################

# String Conversions
 
#Two types of string conversions are required frequently:-Converting the case of characters in string-Converting numbers to string and vice versa
#Case conversions can be done using str methods:
str.upper( ) #converts string to uppercase. 
print(str.upper( ))
str.lower( ) #converts string to lowercase.
print(str.lower( ))
str.capitalize() #converts first character of string to uppercase.
print(str.capitalize())
str.title( ) #converts first character of each word to uppercase.
print(str.title())
str.swapcase() #swap cases in the string.
print(str.swapcase()) 

chr(65) # represents the char of unicode
print(chr( 65 )) 

ord("A") # represents the unicode of char
print(ord("A"))


###############################################################
#string Comparison
s1 = "Bombay" 
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"
print(s1 == s2) # displays False
print(s1 == s5) # displays True
print(s1 != s3) # displays True
print(s1 > s5) # displays False
print(s1 < s2) # displays True
print(s1 <= s4) # displays True

# String comparison is done in lexicographical order (alphabetical) character by character. Capitals are considered to be less than their lowercase counterparts. Result of comparison operation is either True or False.
# Note that there is only one str object containing"Bombay", so s1 and s5both contain the same address.

#####################################################
 
print("#################################################################") 
print("Practice session")

str = "Bamboozled"
print(str[0:2]) # print is done till one less than the value passed after : 

print(str[len(str)-2:]) # print is done from the third last till the end

print(str[::-1]) # reverse string
print(str[0:10:2]) # lasts index is the space between the start and the onwards

print("Question 2")
print("And" in 'And QuietFlows The Don' )