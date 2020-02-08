n = int(input("Please enter a number: "))
num1 = 0
num2 = 1
print(num1, end="")
for i in range(1,n+1):
    num2 = num1 + num2  
    num1 = num2 - num1
    print(",",num2, end="")


# Fibonacci
# Please enter a number: 9
# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55