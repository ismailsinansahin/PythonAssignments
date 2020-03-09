"""
An array inhabitant represents cities and their respective populations. 
For example, the following arrays shows 8 cities and their respective populations:
[3, 6, 0, 4, 3, 2, 7, 1]
Some cities have a population of 0 due to a pandemic zombie disease that is wiping away the human lives. 
After each day, every city will lose half of its population.
write a program to loop through each city population and make it lose half of its population 
until all cities have no humans left. Make updates to each element in the array And print the array
-like below for each day:
Day 0 [3, 6, 0, 4, 3, 2, 7, 1]
Day 1 [1, 3, 0, 2, 1, 1, 3, 0]
Day 2 [0, 1, 0, 1, 0, 0, 1, 0]
Day 3 [0, 0, 0, 0, 0, 0, 0, 0]
---- EXTINCT ----
Write the program in a way that it will handle any number of people in cities, 
above was just an example number to follow.
Hint: 
Below expression will print array in this format:
[3, 6, 0, 4, 3, 2, 7, 1]
"""

populations = [3, 6, 1, 4, 3, 2, 7, 1]
day = 1

print("Day  0", populations)

while sum(populations)>0:
    
    for i in range(len(populations)):
        populations[i] = int(populations[i]/2)
        
    print("Day ", day, populations)
    day += 1
    
print("---------EXTINCT-----------")
    
    
    
    
    
    
