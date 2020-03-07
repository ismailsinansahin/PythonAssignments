"""
You have a word, do the following:
If the word has odd number of characters and has 5 or more characters, 
print the middle three characters of the word. Otherwise, print "invalid".
Sample Output:
       fifteen ==> fte
       apple ==> ppl
       hey ==> invalid
       java ==> invalid
      whatsup ==> ats
      $ ==> invalid
"""

word = str(input("Please enter the word : "))

if len(word) >= 5 and len(word) %2 != 0:
    print(word + "  ==> " + word[len(word)//2-1] +  word[len(word)//2] + word[len(word)//2+1])
else:
    print(word + " ==> invalid")
    