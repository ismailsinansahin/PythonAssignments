row = int(input("Please enter the upper number: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
for i in range(row-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")


# Please enter the upper number: 8

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 