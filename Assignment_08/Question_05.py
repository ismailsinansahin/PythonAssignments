def sign(num):
    if num>0:
        print("1")
    elif num<0:
        print("-1")
    else:
        print("0")
        
num = int(input("Please enter the number: "))
print("sign(" ,num ,") => ",end="")
sign(num)


# Please enter the number: 5
# sign( 5 ) => 1
# Please enter the number: -8
# sign( -8 ) => -1
# Please enter the number: 0
# sign( 0 ) => 0

