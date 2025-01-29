letter = ''' Dear <|Name|>, You are selected! 
<|Date|>
'''

print(letter.replace("<|Name|>", "Apple").replace("<|Date|>", "24 Sept, 2025"))