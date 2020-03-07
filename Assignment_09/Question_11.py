"""
We have a message variable already declared and assigned value in this format
Sender:<Mike Smith>. From Number:[202-123-3456]. Message:{I love programming and problem solving}
Declare variables: sender, phoneNumber, messageBody
By using String methods: retrieve related information from SMS message string 
and assign it to those 3 variables and print each variable in a separate line
Sample Output:
    Sender: Mike Smith
    Phone Number: 202-123-3456
    Message body: I love programming and problem solving
"""

message = input("Please enter the message : ")

sender = message[message.index("<")+1:message.index(">")]
phoneNumber = message[message.index("[")+1:message.index("]")]
messageBody = message[message.index("{")+1:message.index("}")]

print("\nSender            : ", sender)
print("Phone Number  : ", phoneNumber)
print("Message body  : ", messageBody)
