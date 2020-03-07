"""
You have a word, do the following:
1. When word has odd number of characters and:
     - 3 or more characters, print middle letter
              oak ==> a
              javav ==> v
     - Single character, print that character 3 times
             # ==> ###
             q ==> qqq
2. When word has even number of characters and:
     - 4 or more characters, print middle 2
            java ==> av
            apples ==> pl
            #$%^&* ==> %^
    - 2 characters, print those 2 characters twice
           @@ ==>@@@@
           $$ ==>$$$$
           hi ==> hihi
"""

word = str(input("Please enter the word : "))

if len(word) %2 != 0:
    if len(word) == 1:
        print(word + " ==> " + 3 * word)
    else:
        print(word + " ==> " + word[len(word)//2])
if len(word) %2 == 0:
    if len(word) == 2:
        print(word + " ==> " + 2 * word)
    else:
        print(word + " ==> " + word[len(word)//2-1] + word[len(word)//2])