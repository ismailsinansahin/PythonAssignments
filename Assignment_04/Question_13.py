checks = int(input("Howmany checks did you write this month? : "))

if checks < 20:
    fee = checks * 0.10
elif 20 <= checks <= 39:
    fee = checks * 0.08
elif 40 <= checks <= 59:
    fee = checks * 0.06
elif checks >= 60:
    fee = checks * 0.04
else:
    print("Invalid input")
    
print("Your fee is : ", fee)
