"""
Binary number is a number expressed in the base-2 numeral system or binary numeral system,
 which uses only two symbols: typically 0 (zero) and 1 (one). Each digit is referred to as a bit.
Given an int variable decimal, write a java program to calculate the binary value of the 
decimal variable and assign it a binary array. print out the value of binary array matching below format. 
Feel free to use additional arrays or formulas.
Sample Output:
     decimal -> 3
     binary -> [0, 0, 0, 0, 0, 0, 1, 1]
     decimal -> 35
     binary -> [0, 0, 1, 0, 0, 0, 1, 1]
     decimal -> 255
     binary -> [1, 1, 1, 1, 1, 1, 1, 1]
"""

decimal = int(input("Please enter a number : "))
print("decimal : ", decimal)
print("binary   : ", bin(decimal))