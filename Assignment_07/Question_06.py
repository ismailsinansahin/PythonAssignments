row = int(input("Please enter the upper number: "))

for i in range(1,row+1):
    total = i
    for j in range(1,i+1):
        print(total,end=" ")
        total += row-j       
    print("")
    
    
# Please enter the upper number: 10

# 1 
# 2 11 
# 3 12 20 
# 4 13 21 28 
# 5 14 22 29 35 
# 6 15 23 30 36 41 
# 7 16 24 31 37 42 46 
# 8 17 25 32 38 43 47 50 
# 9 18 26 33 39 44 48 51 53 
# 10 19 27 34 40 45 49 52 54 55 
