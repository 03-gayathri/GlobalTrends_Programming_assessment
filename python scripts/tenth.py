''' code to create a python function that takes 2D list and returns its transpose'''
def transpose_matrix(matrix):

    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [
    [4, 5, 3, 9],
    [7, 1, 8, 2],
    [5, 6, 4, 7]
]

transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
