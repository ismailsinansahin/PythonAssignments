"""
Given two arrays of ints sorted in increasing order, outer and inner, print out true 
if all of the numbers in inner appear in outer. Take advantage of the fact that both arrays
 are already in sorted order.
Sample Output:
     input (outer): 1, 2, 4, 6
     input (inner): 2, 4
     output: true
     input (outer): 1, 2, 4
     input (inner): 6, 5
     output: false
"""

def appear(outer, inner):

    for each in inner:
        if each not in outer:
            return False
        else:
            return True

#  MAIN

outer1 = [1,2,4,6] 
inner1 = [2,4] 
outer2 = [1,2,3,4] 
inner2 = [6,5]

print("\ninput   -> ", outer1)
print("input   -> ", inner1)
print("output -> ", appear(outer1,inner1))
print("\ninput   -> ", outer2)
print("input   -> ", inner2)
print("output -> ", appear(outer2, inner2))
