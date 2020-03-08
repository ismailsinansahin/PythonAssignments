"""
Return the number of times that the string "java" appears anywhere in the given string word.
Sample Output:
     input: javaxjava
     output: 2
     input: javaxjavaapplepearjavaegg
     output: 3
"""

text = input("Please enter your text : ").lower()
print("input   : ", text)
print("output : ", text.count("java"))