"""
You have 2 words, both of them have 3 characters.
If either of them does not have exactly 3 characters, print "cannot merge". 
Merge their characters one by one and print together like below:
Sample Output:
     aok
     lol
     alookl

     ear
     pie
    epaire

    java
    wow
    cannot merge
"""

word1 = str(input("Please enter the first 3 characters of word : "))
word2 = str(input("Please enter the second  3 characters of word : "))

print("\nmerged word ==> ", end="")

if len(word1)==3 and len(word2)==3:
    for i in range(3):
        print (word1[i] + word2[i], end="")
else:
    print("cannot merge")
    
    