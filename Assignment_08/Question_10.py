def isEven(num):
    
    if num%2==0:
        return True
    else:
        return False
    
num = int(input("Please enter the number: "))
print("isEven(", num, ") --> ", isEven(num))


# Please enter the number: 9
# isEven( 9 ) -->  False

# Please enter the number: 24
# isEven( 24 ) -->  True
