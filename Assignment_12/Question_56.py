"""
Modify an array that is "left shifted" by one -- so {6, 2, 5, 3} becomes {2, 5, 3, 6}. 
You may modify and print the given array, or print a new array.
Sample Output:
     input: 6, 2, 5, 3
     output: [2, 5, 3, 6]
"""

arr = [6,2,5,3]
print("input   : ", arr)

temp = arr[0]
for i in range(len(arr)-1):
    arr[i] = arr[i+1]
arr[len(arr)-1] = temp

print("output : ", arr)