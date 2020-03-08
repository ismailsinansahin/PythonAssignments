"""
Given a string, print out true if the number of appearances of "java" anywhere in the 
string is equal to the number of appearances of "python" anywhere in the string (case sensitive).
Sample Output:
     input: We study java not python
     output: true
     input: What's the difference between java, javascript and python?
     output: false
"""

text = input("Please enter the text : ")
print("input   : ", text)
print("output : ", text.count("java") == text.count("python"))