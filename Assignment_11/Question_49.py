"""
Given an int array of any length, print a new array of its first 2 elements. 
If the array is smaller than length 2, use whatever elements are present.
Sample Output:
     input 1, 2, 3 
     output: [1, 2]
     input 1,
     output: [1]
"""

def first2(arr):

    if len(arr) <= 2:
        return arr
    else:
        arr = arr[:2]
        return arr

#  MAIN

arr1 = [1,2,3] 
arr2 = [1] 

print("\ninput   -> ", arr1)
print("output -> ", first2(arr1))
print("\ninput   -> ", arr2)
print("output -> ", first2(arr2))