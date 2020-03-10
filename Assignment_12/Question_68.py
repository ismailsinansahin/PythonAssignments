"""
Method addElements accepts 2 int arrays and adds each element value of two arrays 
and returns a new array. You can assume that each array has 5 elements
addElements(new int[][10, 40, 50, 3, 1],
new int[][11, 0, 500, 44, 1101]);
--------
return array after adding values in the arrays:
[21, 40, 550, 47, 1102]
"""

def addElements(arr1, arr2):
    
    newInt = []
    
    for i in range(5):
        newInt.append( arr1[i] + arr2[i])
   
    return newInt
   
#  MAIN
    
arr1 = [10, 40, 50, 3, 1]
arr2 = [11, 0, 500, 44, 1101]

print("\ninput   : ", arr1)
print("input   : ", arr2)

print("output : ", addElements(arr1, arr2))