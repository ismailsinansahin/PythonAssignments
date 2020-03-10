"""
Given a 2d array of ints, find the biggest number(integer) and 
replace all array values on the biggest number in the array then print an array.
Sample Output:
     Given values: [[1, 2, 3], [5, 33, 9]]
     output: [[33, 33, 33], [33, 33, 33]]
"""

arr = [[1, 2, 3], [5, 33, 9]]
print("input   : ", arr)

maxValue = arr[0][0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]  >  maxValue:
            maxValue = arr[i][j]
            
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = maxValue
        
print("output : ", arr)
