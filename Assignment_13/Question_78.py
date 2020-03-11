"""
Reverse a vowels of string without affecting any other characters. 
Write a method reverseVowels() that will return a string with reversed vowels.
Sample Output:
     Input: str = "apple"
     Output: str = "eppla"
     Input: str = "Ab,c,de!$"
     Output: str = "eb,c,dA!$"
     Input : hello world
     Output : hollo werld
Note that only vowels were reversed.
"""

def reverseVowels(word):
    
    vowels = ["a", "e", "i", "o", "u"]
    temp = []
    word = list(word)
       
    for i in range(len(word)):
        if word[i].lower() in vowels:
            temp.append(word[i])
    
    t = len(temp)-1
    
    for i in range(len(word)):
        if word[i].lower() in vowels:
            word[i] = temp[t]
            t -= 1

    return("".join(word))

#  MAIN

word1 = "apple"
word2 = "Ab,c,de!$"
word3 = "hello world"   
     
print("\ninput   : ", word1)
print("output : ",reverseVowels(word1))

      
print("\ninput   : ", word2)
print("output : ", reverseVowels(word2))
      
print("\ninput   : ", word3)
print("output : ", reverseVowels(word3))
