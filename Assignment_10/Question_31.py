"""
Palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
So method isPalindrome checks that and returns true if check is palindrome and false if it is not.
- make your conditions case insensitive. ex: Civic and civic are both palindromes
- make your conditions space insensitive. Race car is a palindrome even though there is space in between.
Sample Output:
     isPalindrome("Noon") ==> true
     isPalindrome("I am not palindrome") ==> false
     isPalindrome("wooden") ==> false
     isPalindrome("Nurses Run") ==> true
"""

def isPalindrome(word):
    
    return word ==  "".join(reversed(word))

# MAIN

word = input("Please enter the word : ")
print("\nisPalindrome(\"", word, "\") ==> ",  isPalindrome(word.lower().replace(" ","")))
