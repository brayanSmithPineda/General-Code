"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
h = matrix[0]
h
s = matrix.pop(0)
s
t = []
t.append(s)
t
m = matrix.pop()[::-1]
m
Matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

s = Matrix.pop(0)
s
def spiralOrder(matrix):
    result = []
    while matrix:
        # Right
        result += matrix.pop(0)

        # Down
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Left
        if matrix:
            result += matrix.pop()[::-1]

        # Up
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))
                
    return result

spiralOrder(matrix=Matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix)

matrix = [[None]]

def matrixvacia(matrix):
    return matrix == None
matrixvacia(matrix)

#loop while the matrix is not empty
#get the elements of the top, pop them from the matrix and append them to the result
#get the last elements of the remaining rows of the matrix, pop them and add it to the result
#get the elements fo the last row in reverse order, pop them and append them to the result
#finally get the elements of the first column of the remaing rows, pop and add it to the result

def spiral_matrix(matrix):
    result = []
    while matrix:
        #Get the elements of the top row
        result += matrix.pop(0)

        #Get the last elements of the remaining rows
        if matrix and matrix[0]: #this condtion ensure that there is element in the matrix and the row, so we can get the elements
            for row in matrix:
                result += row.pop()
        
        #Get the elements of the last row in reversed order
        if matrix:
            result += matrix.pop()[::-1] #Matrix.pop get the last row in the matrix and pop them, and then the slicing get the elements in reversed order

        #Finally we get the elemnts of the first column
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result += row.pop()

    return result
result = [1,2,3,4,10,13,17,16,15,14,9,5]
matrix = [[1,2,3,4],[5,6,7,10],[9,11,12,13],[14,15,16,17]]
spiral_matrix(matrix)
matrix.pop(0)
for row in matrix:
    row.pop()
matrix
matrix.pop()[::-1]
for row in matrix[::-1]:
    row.pop(0)