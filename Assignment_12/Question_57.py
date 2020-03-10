"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1+5+9 = 15. 
The right to left diagonal = 3+5+9 = 17. 
Their absolute difference is |15-17| = 2.
"""

matrix = [[1,2,3],[4,5,6],[9,8,9]]
print("\nmatrix ==> ", matrix)

total1 = 0
total2 = 0

for i in range(len(matrix)):
    total1 += matrix[i][i]
    total2 += matrix[i][len(matrix)-1-i]
    
print("Absolute difference is : ", abs(total1-total2))
    