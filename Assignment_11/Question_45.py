"""
Write a program that will print the shortest word in the given array str.
Sample Output:
     input: java, cable, red, vivid, remedy, grace
     output: red
"""

words = ["java", "cable", "red", "vivid", "remedy", "grace"]


print("\nwords      -> ", words)
shortest = words[0]

for each in words:
    if len(each) < len(shortest):
        shortest = each
        
print("\nshortest -> ", shortest)


