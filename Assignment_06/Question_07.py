row = int(input("Please enter the upper bound: "))
for i in range(row,0,-1):
    for j in range(1,row-i+1):
        print("  ",end="")
    for k in range(i,0,-1):
        print(str(k), "  ",end="")
    print("")
    
# Please enter the upper bound: 5

# 5   4   3   2   1   
#   4   3   2   1   
#     3   2   1   
#       2   1   
#         1  