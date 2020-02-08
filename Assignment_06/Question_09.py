for i in range(1,9):
    if i%2==0:       
        for j in range(1,9):
            if j%2==0:
                print("W",end=" ")
            else:
                print("B",end=" ")
        print("")
    else:
        for j in range(1,9):
            if j%2==0:
                print("B",end=" ")
            else:
                print("W",end=" ")
        print("")
        

# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 