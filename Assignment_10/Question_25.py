"""
When gears merge and work together, one tooth from each one goes in order.
Write a method mergeStrings that will return the strings merged, 
one letter at a time, starting with one. Please note one and two can be of different lengths.
 Please look at below examples:
     s1 ==> "12345"
     s2 ==> "abcde"
     mergeStrings(s1,s2) ==> "1a2b3c4d5e"
     mergeStrings("wooden", "spoon") ==> "wsopoodoenn"
     mergeStrings("java", "selenium") ==> "jsaevlaenium
"""

def mergeStrings(s1,s2):
    
    merged = ""
    minLength = min(len(s1),len(s2))
    
    for i in range(minLength):
        merged += s1[i]+s2[i]

    if len(s1) > len(s2):
        merged += s1[minLength:]
    else:
        merged += s2[minLength:]
        
    return merged

#  MAIN 

s1 = input("Please enter the first string   : ")
s2 = input("Please enter the second string : ")
print("\nmergeStrings(", s1, ",", s2, ") ==> ", mergeStrings(s1,s2))