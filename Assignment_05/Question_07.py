num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

print("num1 = ", num1)
print("num2 = ", num2)
print("num3 = ", num3)

if num1<num2 and num1<num3:
    if num2<num3:
        print("Medium value is: ", num2)
    else:
        print("Medium value is: ", num3)
elif num2<num1 and num2<num3:
    if num1<num3:
        print("Medium value is: ", num1)
    else:
        print("Medium value is: ", num3)
elif num3<num1 and num3<num2:
    if num1<num2:
        print("Medium value is: ", num1)
    else:
        print("Medium value is: ", num2)
else:
    print("There is an equality in the number. There is no medium value...")