"""
This method gets two strings (text and badWord) and returns a string. 
Basicly what it does is take out all the occurrences of badWord in text.
Sample Output:
     clean ("one two three","two")
     returns "one three"
     clean ("foo bar","foo")
     returns "bar"
     clean ("he said bla bla bla","bla")
     returns "he said "
"""

def clean(word, badWord):
    
    return word.replace(badWord, "")

# MAIN

word = input("Please enter the word : ")
badWord = input("Please enter the badword you want to clean : ")
print("\nclean(\"", word, "\" , \"", badWord, "\") ==> ",  clean(word, badWord))
