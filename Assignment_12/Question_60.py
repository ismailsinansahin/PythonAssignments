"""
combine two String arrays into one arraylist and return it as a string.
Sample Output:
     combineRs(["f","o","o"],[" b","a","r"])
     returns "foo bar"
     combineRs(["1","2","3"],[" 4"])
     returns "1234"
"""

def combineRs(arr):
    
    word = ""
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            word += (arr[i][j])
    
    return word 

#  MAIN
    
arr1 = [["f","o","o"],[" b","a","r"]]
print("\ninput   :", arr1)
print("output : ", combineRs(arr1))

arr2 = [["1","2","3"],[" 4"]]
print("\ninput   :", arr2)
print("output : ", combineRs(arr2))