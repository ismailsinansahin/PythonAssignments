"""
A sandwich is two pieces of bread with something in between. 
Print the string that is between the first and last appearance of "bread" in the given string, 
or return string "nothing" if there are not two pieces of bread.
Sample Output:
     input: breadjambread
     output: jam
     input: xxbreadjambreadyy
     output: jam
     input: xxbreadapple
     output: nothing
     input: breadbutterbread
     output: butter
"""

text = input("Please enter the text : ")
print("input   : ", text)
beginIndex =  text.find("bread")+5
endIndex = text.find("bread",text.find("bread")+5)
if endIndex == -1:
    print("output : nothing")
else:
    print("output : ", text[beginIndex:endIndex])