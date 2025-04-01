with open("donkey.txt", "r") as f:
     content = f.read()
         
updated_content = content.replace("donkey", "#####")

with open("donkey.txt", "w") as f:
    f.write(updated_content)
      
# note : don't put the if condition in the while reading the file, other whole file will be deleted.

# reason : 
# if "donkey" in f.read():
#     content = f.read()
# Problem: f.read() Moves the File Pointer
# When you call f.read(), it reads the entire file and moves the file pointer to the end. So when you try to read it again with content = f.read(), there’s nothing left to read, and content becomes an empty string.
      
      
         
        
        

        
