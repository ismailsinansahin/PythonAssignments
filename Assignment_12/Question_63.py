"""
Write a method that will take an argument of ArrayList of Doubles called doubles, 
and remove the first two elements in ArrayList and return the final list.
"""

def doubles(arr):
    return arr[2:]  
   
#  MAIN
    
arr = [1.5,2.6,3.8,4.9]
print("\ninput   : ", arr)
print("output : ", doubles(arr))