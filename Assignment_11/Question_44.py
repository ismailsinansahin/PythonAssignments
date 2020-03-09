"""
Given an array temps of doubles, containing temperature data, compute the average temperature.  
Sample Output:
     input: 80 88 88 84 82 78 60 68
     output: 78.5
"""

temp = [80, 88, 88, 84, 82, 78, 60, 68]
print("\ninput :   ", temp)
print("output : ", sum(temp) / len(temp))

