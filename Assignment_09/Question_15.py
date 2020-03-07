"""
Print true if the string "cat" and "dog" appear the same number of times in the given string word.
Sample Output:
     input: catdog
     output: true
     input: catcat
     output: false
     input: cat-cheetah-dog-cat
     output: false
"""

word = input("Please enter the word : ").lower()
print("input   : ", word)
print("output : ", word.count("dog") == word.count("cat"))
