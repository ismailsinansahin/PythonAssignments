"""
This method gets an arraylist of Integers and a number(Integer).
it returns an arraylist. It removes any instance of the number it gets from the arraylist.
Sample Output:
     romoveInst([1,1,2,3,1,4],1)
     returns: [2,3,4]
     romoveInst([3,4,3,3],4)
     returns: [3,3,3]
"""

def removeInst(arr, number):
    
    newArr = []
    
    for i in range(len(arr)):
        if arr[i] != number:
            newArr.append(arr[i])
    
    return(newArr)

#  MAIN
    
arr1 = [1,1,2,3,1,4]
number1 = 1

arr2 = [3,4,3,3]
number2 = 4
    
print("\narr1      : ", arr1)
print("number1 : ", number1)
print("returns : ", removeInst(arr1, number1))
print("\narr2      : ", arr2)
print("number2 : ", number2)
print("returns : ", removeInst(arr2, number2))