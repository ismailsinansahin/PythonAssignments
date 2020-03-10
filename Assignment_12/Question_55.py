"""
Given an 8x8 two-dimensional array of strings named chessboard. 
Initialize values inside an array accordingly to the chessboard. 
So first element in the array, chessboard[0][0] should have value "1a", 
and the last element in the array, chessboard[7][7] should have value "8h".
Sample Output:
[[1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h], [2a, 2b, 2c, 2d, 2e, 2f, 2g, 2h], 
 [3a, 3b, 3c, 3d, 3e, 3f, 3g, 3h], [4a, 4b, 4c, 4d, 4e, 4f, 4g, 4h], 
 [5a, 5b, 5c, 5d, 5e, 5f, 5g, 5h], [6a, 6b, 6c, 6d, 6e, 6f, 6g, 6h], 
 [7a, 7b, 7c, 7d, 7e, 7f, 7g, 7h], [8a, 8b, 8c, 8d, 8e, 8f, 8g, 8h]]
"""

arr1 = ["a", "b", "c", "d", "e","f", "g", "h"]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
chessboard = []

for i in range(8):
    for j in range(8):
        combined = arr1[i] + str(arr2[j])
        chessboard.append(combined)

print("chessboard ==> ", chessboard)