"""
coverString method will take 2 string parameters from the caller.
Your job is to write an important code that will :
- to search and find each appearance of coverME within main
- then surround it with [coverMe] (square brackets)
- if you cannot find the coverME within main after tirelessly looping 
then just return whole main itself covered [main].
- keep in mind that coverME value can be of any length.
Sample Output:
     coverString("java methods", "me") ) ; ==> "java [me]thods"
     coverString("Certified Wooden Spoon", "o") ) ; ==> "Certified W[o][o]den Sp[o][o]n"
     coverString("hello hello", "ello") ) ; ==> "h[ello] h[ello]"
     coverString("apples", "pears") ) ; ==> "[apples]"
"""

def coverString(word, wordCovered):
    
    return word.replace(wordCovered, "[" + wordCovered + "]")

# MAIN

word = input("Please enter the word : ")
wordCovered = input("Please enter the value will be covered : ")
print("\ncoverString(\"", word, "\" , \"", wordCovered, "\") ==> ",  coverString(word, wordCovered))