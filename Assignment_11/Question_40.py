"""
Given the array words, it will print the word with the largest length. 
Assume that there are no 2 words with longest length
Sample output:
     words -> ["aaa", "bbbbb", "whasstupppp", "longg" , "jaaaaavvaaaaaaaaaa"]
     prints jaaaaavvaaaaaaaaaa
"""

arr = ["aaa", "bbbbb", "whasstupppp", "longg" , "jaaaaavvaaaaaaaaaa"]
print("arr ==> ", arr)

for i in range(len(arr)-1):
    max = arr[i]
    if len(arr[i+1]) > len(arr[i]):
        max = arr[i+1]
        
print("\nmax ==> ", max)