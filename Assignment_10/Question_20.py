"""
In mathematics, the factorial of a positive integer n, denoted by n!,  
is the product of all positive integers less than or equal to n.
Calculate factorial and output result to the console. 
Sample Output:
     input: 5
     output: 120
"""

import math
number = int(input("Please enter a number : "))
print("input   : ", number)
print("output : ", math.factorial(number))