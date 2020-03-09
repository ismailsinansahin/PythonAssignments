"""
Given an int array, print a new array with double the length where its last element is the same 
as the original array, and all the other elements are 0. The original array will be length 1 or more. 
Note: by default, a new int array contains all 0's.
Sample Output:
     input: 4 5 6
     output: [0, 0, 0, 0, 0, 6]
     input: 0
     output: [0, 0]
     input: 1 2 3 4
     output: [0, 0, 0, 0, 0, 0, 0, 4]
"""

def times2Last(arr):

    arr.extend(arr)
    for i in range (len(arr)-1):
        arr[i] = 0
    return arr

#  MAIN

arr1 = [4,5,6] 
arr2 = [0] 
arr3 = [1,2,3,4] 

print("\ninput   -> ", arr1)
print("output -> ", times2Last(arr1))
print("\ninput   -> ", arr2)
print("output -> ", times2Last(arr2))
print("\ninput   -> ", arr3)
print("output -> ", times2Last(arr3))