words = ["donkey", "horse", "animal"]

with open("donkey.txt", "r") as f:
    content = f.read()
         
for word in words:        
    content = content.replace(word, "#" * len(word)) 
    # must replace in content so that each change can be seen in the main file, not use the updated_content variable.

with open("donkey.txt", "w") as f:
    f.write(content)