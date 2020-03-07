"""
Write a program that will print out information about the user based on email. 
Print first and last name from the upper case.
Sample Output:
     Input: craig_federighi@apple.com
    Output: 
           First name: Craig
           Last name: Federighi
           Domain: apple
           Top-Level Domain: com
"""

email = input("Please enter the email : ")

firstName = email.split("@")[0].split("_")[0].title()
lastName = email.split("@")[0].split("_")[1].title()
domain = email.split("@")[1].split(".")[0]
topLevelDomain = email.split("@")[1].split(".")[1]

print("First name            : ", firstName)
print("Last name              : ", lastName)
print("Domain                  : ", domain)
print("Top-Level Domain : ", topLevelDomain)