"""
Given two strings, word and a separator sep, return a big string made of count 
occurrences of the word, separated by the separator string.
Sample Output:
     input: Word
     input: X
     input: 3
     output: WordXWordXWord
     input: This
     input: And
     input: 2
     output: ThisAndThis
     input: This
     input: And
     input: 1
     output: This
"""

word = input("Please enter the word : ")
sep = input("Please enter the seperator : ")
number = int(input("Howmany times do you want to print your word? : "))
print("input   : ", word)
print("input   : ", sep)
print("input   : ", number)
print("output : ", (number-1) * (word+sep) + word)