"""
Search method accepts ArrayList of Strings and  a String to find and returns a String.
It will look for an element within ArrayList that contains the value of the find. 
If it finds it, the method needs to return the whole Element value. 
If an instance of find doesn't exist return: "search failed"
Sample Output:
    search(["one apple","two orange","four banana"],"four")
      returns:
     "four banana"
     ("four banana" contains "four" so method returns "four banana")
     search(["hello","world"],"goodbye")
     returns:
     "search failed"
     (no "goodbye" in any element)
"""

def search(arr, word):

    for i in range(len(arr)):
        if word in arr[i]:
            a = arr[i]
            break
        else:
            a = "Search Failed"
            
    return(a)

#  MAIN
    
arr1 = ["one apple","two orange","four banana"]
word1 = "four"

arr2 = ["hello","world"]
word2 = "goodbye"
    
print("\narr1      : ", arr1)
print("number1 : ", word1)
print("returns : ", search(arr1, word1))
print("\narr2      : ", arr2)
print("number2 : ", word2)
print("returns : ", search(arr2, word2))