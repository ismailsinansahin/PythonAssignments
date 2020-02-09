def fib(num):
    
    num1=0
    num2=1
    
    for i in range(1,num-1):       
        num2 += num1    
        num1 = num2-num1
    return num2
             
num = int(input("Please enter a number: "))
print("Input  : ", num)
print("Output : ", fib(num))


# Please enter a number: 9
# Input  :  9
# Output :  21