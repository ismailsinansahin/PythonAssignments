"""
Given a String array words, iterate through each word and print the first and 
the last letter of each element in separate lines.
Sample output:
     words → ["hello", "why", "by", "apple" , "note"]
     print: 
     ho
     wy
     by
     ae
     ne
"""

def firstLast(arr):
    
    print("print:")
    for i in range(5):
        print(arr[i][:1] + arr[i][-1:])
    
#  MAIN
   
arr = ("hello", "why", "by", "apple", "note")
print("arr = ", arr, " ==> ")
firstLast(arr)
