"""
t3 method gets two strings and returns a string. 
The first string is the one that will be manipulated. 
At the 3rd char position of the target you will insert the word argument.
Sample output:
     at3("longword","foo")
     return: "lonfoogword"
     at3("blabla","a")
     return: "blaabla"
"""

def at3(word, inserting):
    
    return word[:3] + inserting + word[3:]

# MAIN

word = input("Please enter the word : ")
inserting = input("Please enter the word you want to insert : ")
print("\nat3(\"", word, "\" , \"", inserting, "\") ==> ",  at3(word, inserting))