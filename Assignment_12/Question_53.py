"""
In the sport of diving, seven judges award a score between 0 and 10, 
where each score may be a floating-point value. 
The highest and lowest scores are thrown out, and the remaining scores are added together. 
The sum is then multiplied by the degree of difficulty for that dive. 
The degree of difficulty ranges from 1.2 to 3.8 points. 
The total is then multiplied by 0.6 to determine the divers' score.
Use System.out.printf("Total: %.2f",total); in order to get rid of extra floating points.
Sample Output:
     output: Enter score for judge 1:
     input: 1
     output: Enter score for judge 2:
     input: 5
     output: Enter score for judge 3:
     input: 5
     output: Enter score for judge 4:
     input: 5
     output: Enter score for judge 5:
     input: 5
     output: Enter score for judge 6:
     input: 8
     output: Enter score for judge 7:
     input: 9
     output: Enter difficulty:
     input: 2.1
     output: Total: 35.28
"""

scores = []
i = 1

while i <= 7:
    print("\nJudge ", i, end="")
    score = int(input("Enter your score between 0-10 : "))
    if 0 <= score <= 10:
        scores.append(score)
        i += 1

scores.sort()
scores = scores[1:6]
    
difficulty = 0
while not 1.2 <= difficulty <= 3.8:
    difficulty = float(input("Enter difficulty between 1.2 - 3.8 : "))

total = sum(scores) * difficulty * 0.6
print("\nTotal Score : ", total)





















