"""
Create a method that is called "twoTimes" takes in a single parameter 
- an ArrayList of Integers and returns a new ArrayList of Integers
This method should create a new ArrayList of Integers that contains every value of the 
ArrayList parameter repeated twice.
For example, if the parameter is
(1,5,3,7)
The method should return a new ArrayList of Integers with
(1,1,5,5,3,3,7,7)
"""

def twoTimes(arr):
    
    newArr = []
    
    for each in arr:
        newArr.append(each)
        newArr.append(each)
            
    return(newArr)

#  MAIN
    
arr= [1,5,3,7]  
print("arr        : ", arr)
print("returns : ", twoTimes(arr))
