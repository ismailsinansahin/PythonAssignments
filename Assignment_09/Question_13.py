"""
Write a program that will print out route instructions. 
Your program should take 2 parameters: start point and endpoint. 
Use left, right, up and down for navigation. Insert ">" between commands. 
If start point equals to endpoint - display: "start/end(start or end variable!) found".
Note: you may move only clockwise.
Sample Output:
     Input: A
     Input: D
     Output: right > down > left: D found
     Input: C
     Input: C
     Output: C found
"""

route = "ABCDABC"
sp = input("Please enter the start point : ").upper()
ep = input("Please enter the end point    : ").upper()

print("\nOutput = ", end="")

for each in route[route.index(sp):]:
    if each != ep:
        if each == "A":           
            print("right  > ", end="")
        if each == "B":           
            print("down  > ", end="")
        if each == "C":           
            print("left  > ", end="")
        if each == "D":           
            print("up  > ", end="")
    else:
        print(each, "found")
        break

