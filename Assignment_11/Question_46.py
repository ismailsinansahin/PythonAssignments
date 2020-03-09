"""
Write a program that will find out the shortest words in the given string str. 
If there are few words that are evenly short, print them all.
 Use the split method in order to split the str string variable and create an array of strings. 
 Print array with Arrays.toString() method. Sort array before printing.
Sample Output:
     input: olive, fish, pursuit, old, warning, python, java, coffee, cat, ray
     output: [cat, old, ray]
"""

words = ["olive", "fish", "pursuit", "old", "warning", "python", "java", "coffee", "cat", "ray"]

print("\nwords     -> ", words)
shortest = len(words[0])
shorts = []

for each in words:
    if len(each) < shortest:
        shortest = len(each)

for each in words:
    if len(each) == shortest:      
        shorts.append(each)
        
print("shortest -> ", shorts)
        
