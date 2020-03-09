"""
Given a String variable sentence, write code to type each word in separate lines in reverse order.
Sample output:
     sentence -> "Java is fun"
     Print:
     fun
     is
     Java
"""
   
sentence = input("Please enter the sentence : ")
sentence = sentence.split()

for i in reversed(range(len(sentence))):
    print(sentence[i])
