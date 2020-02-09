row = int(input("Please enter the upper number: "))

for i in range(1,row+1):
    for j in range(0,i):
        print(" ",end="")
    for k in range (1,row-i+2):
        print(k,end=" ")
    print("")  
for i in range(2,row+1):
    for j in range(row-i+1,0,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print("")
    
    
# Please enter the upper number: 7

#  1 2 3 4 5 6 7 
#   1 2 3 4 5 6 
#    1 2 3 4 5 
#     1 2 3 4 
#      1 2 3 
#       1 2 
#        1 
#       1 2 
#      1 2 3 
#     1 2 3 4 
#    1 2 3 4 5 
#   1 2 3 4 5 6 
#  1 2 3 4 5 6 7 

