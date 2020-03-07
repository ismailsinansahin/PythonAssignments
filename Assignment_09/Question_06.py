"""
Write a program that will reverse a string. 
Your program should reverse a string only 5 characters long. 
If the word is shorter, display message: "Too short!". 
If the word is longer, display the message: "Too long!". 
Otherwise, reverse this word and print out the result into the console.
Sample Output:
     input: cat
     output: Too short!
     input: singularity
     output: Too long!
     input: apple
     output: elppa
"""

word = str(input("Please enter a 5 characters of word : "))
print(word + " ==> ", end="")

if len(word) == 5:
    print("".join(reversed(word)))
elif len(word) > 5:
    print("Too long")
else:
    print("Too short")