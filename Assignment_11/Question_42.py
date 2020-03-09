"""
Given a String array arr with the following elements ["zero", "one", "two","three","four"]
Create another array fewValues and copy words that have letter "e" in them. 
You need to know how many element contain "e" and create array accordingly
Values in fewValues array need to be["zero", "one","three"]
Sample Output::
     arr -> ["aa", "be", "lol", "lel", "oreo"] 
     fewValues -> ["be", "lel", "oreo"]
     arr -> ["e", "hey", "bye", "furey", "spoon"] 
     fewValues ->["e", "hey", "bye", "furey"]
"""

def fewValues(arr):
    
    newArr = []
    
    for each in arr:
        
        if each.count("e") > 0:
            newArr.append(each)
            
    return newArr

#  MAIN

arr1 = ["aa", "be", "lol", "lel", "oreo"] 
arr2 = ["e", "hey", "bye", "furey", "spoon"] 

print("\narr1 -> ", arr1)
print("fewValues -> ", fewValues(arr1))
print("\narr2 -> ", arr2)
print("fewValues -> ", fewValues(arr2))