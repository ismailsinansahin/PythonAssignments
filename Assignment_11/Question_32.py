"""
The code provided in your main method will take in five Strings and save them into an array called arr. 
Print out the first three letters of each element of arr, one per line. 
You can assume that every element of arr is at least 3 letters long.
Sample Output:
     arr -> ["apple", "banana"] 
     prints: app
                  ban
"""

def first3(arr):
    
    print("prints :")  
    for i in range(5):
        print(arr[i][:3])
    
#  MAIN
   
arr = ("apple", "banana", "orange", "watermelon", "strawberry")
print("arr = ", arr, " ==> ")
first3(arr)

