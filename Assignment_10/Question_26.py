"""
uniqueChars is a method that you will code now, should be able to accept any string in the word 
and return unique characters from the parameter.
Sample Output:
     uniqueChars("java") ==> "jav"
     uniqueChars("mama") ==> "ma"
     uniqueChars("spoon") ==> "spon"
"""
def uniqueChars(word):
    
    unique = ""
    
    for each in word:
        if each not in unique:
            unique += each
    
    return unique

# MAIN

word = input("Please enter the word : ")
print("uniqueChars(\"", word, "\") ==> ",  uniqueChars(word))