"""
Create a method that is called removeAll takes two parameters: 
an ArrayList of Strings called wordList, and a String called targetWord and returns nothing
This method should go through every element of wordList and 
remove every instance of targetWord from the ArrayList.
"""

def removeAll(arr, targetWord):
    for each in arr:
        if each == targetWord:
            arr.remove(each)
    
    return arr
   
#  MAIN
    
arr = ["a", "b", "c", "a", "h", "b", "c", "a"]
print("\ninput     : ", arr)
targetWord = input("Please enter the target word : ")
print("\nTarget Word : ", targetWord)
print("\noutput : ", removeAll(arr, targetWord))