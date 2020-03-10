"""
Create a method that is called combineAL takes two parameters: 
an ArrayList of Strings called wordList1, and an ArrayList of Strings called wordList2
 and returns an ArrayList
This method should create a new ArrayList of Strings, 
add all the words (in order) from wordList1, then add all the words (in order) from wordList2.
In other words, it is combining all the elements from the two parameters.
"""

def combineAL(wordList1, wordList2):
    
    words = []
    
    words.extend(wordList1)
    words.extend(wordList2)

    return words   
   
#  MAIN
    
wordList1 = ["Ali", "Veli", "Sinan"]
wordList2 = ["Burak", "Tarık", "Melek"]
print("\ninput   : ", wordList1)
print("input   : ", wordList2)
print("output : ", combineAL(wordList1, wordList2))