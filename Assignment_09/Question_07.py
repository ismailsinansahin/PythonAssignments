"""
Write a program that will print out the first half of the word twice.
Sample Output:
     input: java
     output: jaja
"""

word = str(input("Please enter the word : "))
print(word + " ==> ", 2 * (word[0] + word[1]))

