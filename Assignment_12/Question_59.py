"""
mergR merges two arrays into one.
it gets two int arrays and returns an int array
Sample Output:
     mergR([1,2,3],[4,5,6])
     returns [1,2,3,4,5,6]
     mergR([1,2],[6,8])
     returns [1,2,6,8]
"""

def mergR(arr):
    
    newArr = []
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            newArr.append(arr[i][j])
    
    return newArr 

#  MAIN
    
arr1 = [[1,2,3],[4,5,6]]
print("\ninput   :", arr1)
print("output : ", mergR(arr1))

arr2 = [[1,2],[6,8]]
print("\ninput   :", arr2)
print("output : ", mergR(arr2))


