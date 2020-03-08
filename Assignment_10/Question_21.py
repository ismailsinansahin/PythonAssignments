"""
Given a string, consider the prefix string made of the first n chars of the string. 
Does that prefix string appear somewhere else in the string? 
Assume that the string is not empty and that n is in the range from 1 till str.length().
Sample Output:
     input: abXYabc
     input: 1
     output: true
     a appears twice
     input: abXYabc
     input: 2
     output: true
     ab appears twice
     input: abXYabc
     input: 3
     output: false
     abX appears once only
"""

text = input("Please enter your text : ").lower()
prefix = text[0:int(input("Please enter howmany characters do you want to find : "))]
print("\ninput   : ", text)
print("input   : ", len(prefix))
print("output : ", text.count(prefix)>1)
      
      
      