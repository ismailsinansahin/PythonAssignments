row = int(input("Please enter the upper number: "))

for i in range(1,row+1):
    for j in range(1,i+1):
        if j%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print("")


# Please enter the upper number: 7

# 1
# 10
# 101
# 1010
# 10101
# 101010
# 1010101
