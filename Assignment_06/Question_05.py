n = int(input("Please enter the upper bound: "))
for i in range(1,n+1):
    if i % 2 != 0:
        if i == 1:
            print(i,end="")
        else:
            print(",",i,end="")
            

# Please enter the upper bound: 15
# 1, 3, 5, 7, 9, 11, 13, 15

# Please enter the upper bound: 24
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23