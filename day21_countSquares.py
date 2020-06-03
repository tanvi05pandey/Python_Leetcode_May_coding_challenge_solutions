# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#
# Example 1:
#
# Input: matrix =
# [
#     [0,1,1,1],
#     [1,1,1,1],
#     [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

def countSquares(matrix):
    if not matrix or not matrix[0]: return 0
    rows = len(matrix)
    cols = len(matrix[0])
    result = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                if r == 0 or c == 0: # 1st row or 1st column
                    result += 1
                else: # all other rows and cols
                    val = min(matrix[r][c-1], matrix[r-1][c-1], matrix[r-1][c]) + 1
                    result += val
                    matrix[r][c] = val
    return result


print(countSquares(
    [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
))