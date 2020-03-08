"""
This method gets a string and an int, it returns a string.
 What it does is to limit the inputted string to a creating number of characters.
Sample Output:
     limit("abcd",2)
     returns "ab"
     limit("bla bla",3)
     returns "bla"
"""

def limit(word, number):
    
    return word[:number]

# MAIN

word = input("Please enter the word : ")
number = int(input("Please enter the limit : "))
print("\nlimit(\"", word, "\" , \"", number, "\") ==> ",  limit(word, number))

