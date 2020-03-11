"""
short [] scores = {51, 85, 32, 0, 98, 157, 82, 101, 64, 249};
Above array stores the scores of a batsman in his last 10 winnings in the game of cricket.
To know more about cricket, you can visit Wikipedia link: https://en.wikipedia.org/wiki/Cricket
If the score is greater than or equal to 50 but less than 100, it is regarded as a half-century.
If the score is greater than or equal to 100 but less than 200, it is regarded as a century.
If the score is greater than or equal to 200, it is regarded as a double-century.
NOTE: No scenario of the triple-century in this case.
Write the code to print the number of half-centuries, centuries and double-centuries scored by the batsman.
"""

scores = [51, 85, 32, 0, 98, 157, 82, 101, 64, 249]

hc = c = dc = 0

for each in scores:
    if each >= 200:
        dc +=1
    elif each >=100:
        c +=1
    elif each >=50:
        hc +=1

print("\nscores : ", scores)
print("\nHalf-centuries    : ", hc)
print("Centuries             : ", c)
print("Double-enturies  : ", dc)
    
