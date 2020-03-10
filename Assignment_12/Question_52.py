"""
You get a 2d array and you need to find how many two matches there are
and return the number(int) of matches you found.
For example: 1 and 2 are not a match, 2 and 2 are a match.
a match in this case is two numbers in a row that are equal .
Sample output:
     [2,2,1,3,4,5]
     [5,2,3,3,4,5]
     [3,2,3,1,4,5]
     print
     matches: 2
"""

arr = [[2,2,1,3,4,5], [5,2,3,3,4,5], [3,2,3,1,4,5]]
counter = 0
flag = False

for i in range(len(arr)):
    for j in range (len(arr[i])-1):
        if arr[i][j] == arr[i][j+1]:
            counter += 1
            break
print(counter)