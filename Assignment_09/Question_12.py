"""
Given a string word, if the first or last chars are 'x' or 'X', 
print the string without those 'x' or 'X' chars, otherwise print the string unchanged.
Sample output:
     input: xHiX 
     output: Hi
     input: apple 
     output: apple
     input: xUxL
     output: UxL
     input: JavaX
     output: Java
"""

word = input("Please enter the word : ")

if word[0].lower() == "x":
    word = word[1:]
if word[-1].lower() == "x":
    word = word[:-1]
    
print(word)
