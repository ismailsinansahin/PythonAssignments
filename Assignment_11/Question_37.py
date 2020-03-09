"""
Given a String array words, iterate through each word and print first and last 
letter of each element in the format below.
Sample Output:
     words → ["hello", "why", "by", "apple" , "note"]
     print → [ho, wy, by, ae, ne]
"""

words = ["hello", "why", "by", "apple" , "note"]
print("\nwords ==> ", words)

for i in range (len(words)):
    words [i] = words[i][0] + words[i][len(words[i])-1]

print("\nwords ==> ", words)