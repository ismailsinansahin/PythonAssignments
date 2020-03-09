"""
Given a String variable email, write code using split method to print email id and domain in separate lines.
Sample Output:
     email -> info@cybertekschool.com
     Print: 
     Email id: info
     Email domain: cybertekschool.com
If email contains no @ character or multiple @ characters then print invalid email:
     email -> hello-gmail.com
     print: 
     invalid email
     email -> my@fancy@email.com
     print: 
     invalid email
"""
     
def checkEmail(email):
    
    if email.count("@") != 1:
        print("Invalid email")
    else:
        print("Email ID        : ", email.split("@")[0])
        print("Email Domain : ", email.split("@")[1])

#  MAIN
    
email1 = "info@cybertekschool.com"
email2 = "hello-gmail.com"
email3 = "my@fancy@email.com"

print("\nemail1 -> ", email1)
checkEmail(email1)
print("\nemail2 -> ", email2)
checkEmail(email2)
print("\nemail3 -> ", email3)
checkEmail(email3)