"""
Given a string word, print true if "java" appears starting at index 0 or 1 in the string, 
such as with "javaxxx" or "xjavaxx" but not "xxjavaxx". 
The string should be 4 and more characters.
Sample Output:
     input: javapython
     output: true
     input: cjavac++
     output: true
     input: c#javaruby
     output: false
"""

word = input("Please enter the word : ")
print("input   : ", word)
print("output : ", word[0:4] == "java" or word[1:5] == "java")

