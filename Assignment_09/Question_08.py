"""
Alejandro have started learning java, he knows what you know about ifs and strings. 
He has a large number of text emails, going through all of them will take a lot of time. 
To save time he will only read the emails that refer to him by name. 
He wants to write a program that gets a string (the email) and determines 
if his name "Alejandro" appears in that string.
if so it will output "read this mail" else it will output "don't read".
Sample Output:
     input: "dear alejandro.....alot of text"
     output: "read this mail"
     input: "thunder blaz is the best drink in the galaxy..."
     output: "don't read"
     input: "subject: important project, Alejandro we refer to you this ...."
     output: "read this mail"
     """

text = input("Please enter the email : ")     
word = input("Please enter the word to find : ")
if word.lower() in text.lower():
    print("\nRead this mail")
else:
    print("\nDon't read")