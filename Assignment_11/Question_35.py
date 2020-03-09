"""
Given a String variable sentence, write code to get each word and assign it to String reversed in reverse order.
Sample output:
     sentence -> "Java is fun"
     reversed -> "fun is Java"
"""

sentence = input("Please enter the sentence : ")
print("\nsentence ==> ", sentence)
print("reversed ==>  ", end="")
sentence = sentence.split()
for i in reversed(range(len(sentence))):
    print(sentence[i] + " ", end = "")


