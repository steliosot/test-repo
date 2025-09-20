# Matrix Multiplication in Python

def multiply_matrices(A, B):
    # check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")
    
    # initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # perform multiplication
    for i in range(len(A)):          # rows of A
        for j in range(len(B[0])):   # columns of B
            for k in range(len(B)):  # rows of B / columns of A
                result[i][j] += A[i][k] * B[k][j]
    
    return result


# Example usage
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = multiply_matrices(A, B)

print("Result of Matrix Multiplication:")
for row in result:
    print(row)
