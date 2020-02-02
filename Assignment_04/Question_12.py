package = input("What is your package: A, B, or C --> ")
hours = int(input("How many hours did you use internet this month: "))

if package == 'A' or package == 'a':
    if hours > 10:
        charge = 9.95 + (2 * (hours-10))
    else:
        charge = 9.95
elif package == 'B' or package == 'b':
    if hours > 20:
        charge = 13.95 + (1 * (hours - 20))
    else:
        charge = 13.95
elif package == 'C' or package == 'c':
    charge = 19.95
else:
    print("Invalid input")
    
print(f"Your charge for Package {package} is : $", charge)