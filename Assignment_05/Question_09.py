originalNumber = int(input("Please enter the number: "))
number1 = originalNumber
number2 = originalNumber
a = 0
while number1 != 0:
    number1=number1//10
    a += 1
for each in range(1,a+1):
    displayPrompt = number2//(10**(a-1))
    number2 = number2 - (displayPrompt*(10**(a-1)))
    print("Display prompt", displayPrompt)
    a -= 1

     
     
     
     