"""
Scalar multiplication of matrix is the simplest and easiest way to multiply matrix . ,
Basically you get an int 2d array and need to multiply each of its elements by the value 
of parameter n int. And return the same 2D array back.
Sample Output:
matrix = 
[
[1,1,1]
[1,1,2]
]
scalar(matrix,5)
returns(after multiplying each value by 5):
[
[5,5,5]
[5,5,10]
]
--------------------
matrix = 
[
[2,3,5]
[1,1,2]
]
scalar(matrix,2)
returns:
[
[4,6,10]
[2,2,4]
]
"""

def scalar(matrix, num):
    for i in range(len(matrix)):
       for j in range(len(matrix[i])):
            matrix[i][j] *= num
    
    return matrix

#  MAIN
    
matrix1 = [[1,1,1],[1,1,2]]
num1 = 5

matrix2 = [[2,3,4],[1,1,2]]
num2 = 2


print("\nmatrix1  : ", matrix1)  
print("num1        : ", num1)
print("output    : ", scalar(matrix1, num1))

print("\nmatrix2  : ", matrix2)  
print("num2        : ", num2)
print("output    : ", scalar(matrix2, num2))
       
       
       
       
       
       
       
       
       
       
       
       