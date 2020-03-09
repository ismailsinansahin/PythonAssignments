"""
Given an array of ints, print true if the array contains a 5 next to a 5 anywhere in the array. 
If no consecutive 5s or no 5s are detected in your code then print false.
Sample output:
     nums → [1, 5, 5, 1, 1] → true
     nums → [1, 8, 5, 5, 0] → true
     nums → [1, 5, 4, 1, 5] → false
     nums → [1, 4, 4, 1, 99] → false
"""

def two5s(arr):
    
    flag = False
    
    for i in range(0,len(arr)-1):
        if arr[i] ==5 and  arr[i+1] == 5:
            flag =  True
            break
            
    return flag

# MAIN
    
arr1 = [5, 5, 1, 1, 1]
arr2 = [1, 8, 5, 5, 1]
arr3 = [1, 6, 4, 5, 5]
arr4 = [1, 4, 4, 1, 99]

print("\narr1  = ", arr1, " ==> ", two5s(arr1))
print("\narr2  = ", arr2, " ==> ", two5s(arr2))
print("\narr3  = ", arr3, " ==> ", two5s(arr3))
print("\narr4  = ", arr4, " ==> ", two5s(arr4))
