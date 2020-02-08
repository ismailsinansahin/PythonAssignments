row = int(input("Please enter the upper bound: "))
for i in range(1,row+1):
    print("#",end="")
    if i!=1: 
        for j in range(1,i):
            print(" ",end="")
    print("#")
    print("")
    
# Please enter the upper bound: 5

# ##

# # #

# #  #

# #   #

# #    #