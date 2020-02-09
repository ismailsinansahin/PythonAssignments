row = int(input("Please enter the upper number: "))

for i in range(1,row+1):
    for j in range(0,row-i):
        print(1,end="")
    for j in range(1,i):
        print(i,end="")
    print("")

    
# Please enter the upper number: 7

# 111111
# 111112
# 111133
# 111444
# 115555
# 166666
# 777777