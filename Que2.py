letter=''' Dear <|name|>
You are selected
<|date|>'''

name= str(input("Enter your name= \n" ))
date= (input("Enter Date= \n"))
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>", date)
print(letter)
