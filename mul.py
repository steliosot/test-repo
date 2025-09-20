# Matrix Operations in Python

def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
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
    [7, 8, 9],
    [10, 11, 12]
]

C = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition (A + B):")
for row in add_matrices(A, B):
    print(row)

print("\nDifference (A - B):")
for row in subtract_matrices(A, B):
    print(row)

print("\nMultiplication (A x C):")
for row in multiply_matrices(A, C):
    print(row)
