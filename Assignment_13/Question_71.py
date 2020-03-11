"""
Create a method called populate that accepts an empty int array and populates it with numbers counting up.
Sample Output:
     populate(new int[3])
     returns:[1,2,3]
     populate(new int[5])
     returns:[1,2,3,4,5]
"""

def populate(arr):
    
    newInt = []

    for i in range(arr[0]):
        newInt.append(i+1)
        
    return newInt
    
#  MAIN
    
arr1 = [3]
arr2 = [5]

print("\ninput   : arr1[3]")
print("output :", populate(arr1))
print("\ninput   : arr2[5]")
print("output :", populate(arr2))
