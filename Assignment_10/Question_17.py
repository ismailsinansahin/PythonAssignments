"""
Write a program that will print out letters in the alphabetic order 
accordingly to the given range within 2 chars.
Sample Output:
     input: A
     input: Z
     output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
     input: a
     input: f
     output: abcdef
     input: a
     input: d
     output: abcd
     input: B
     input: O
     output: BCDEFGHIJKLMNO
"""

alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLower = "abcdefghijklmnopqrstuvwxyz"
sp = input("Please enter the first letter : ")
ep = input("Please enter the last letter : ")
print("input   :", sp)
print("input   :", ep)
if sp.islower():
    print("output :", alphabetLower[alphabetLower.index(sp):alphabetLower.index(ep)+1])
else:
    print("output :", alphabetUpper[alphabetUpper.index(sp):alphabetUpper.index(ep)+1])