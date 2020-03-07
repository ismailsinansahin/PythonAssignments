"""
In this task, you need to swap the first name with the last name in the email.
 If the email doesn't contain underscore - do not anything.
Sample Output:
     input: mike_tyson@gmail.com
     output: tyson_mike@gmail.com
     input: barakobama@gmail.com
     output: barakobama@gmail.com
"""

email = input("Please enter the email :")

if "_" in email:
    part1  = email.split("@")[0].split("_")
    part2 = email.split("@")[1]
    email = part1[1] + "_" + part1[0] + "@" + part2
    print("email ==> ", email)
else:
    print("email ==> ", email)