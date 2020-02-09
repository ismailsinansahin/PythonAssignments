def isPalindrome(num):
    
    reverse = 0
    number = num

    while number>0:
        remainder = number%10
        reverse = (reverse*10)+remainder
        number = number//10
        
    if num==reverse:
        return True
    else:
        return False
  
num = int(input("Please enter a number: ")) 
print(isPalindrome(num))


# Please enter a number: 10001
# True