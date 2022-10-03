import numpy as np

def adding_two_matrices(A, B):
    # This functions returns the result from the sum of matrix A with matrix B

    # Make sure we have numpy matrices (type cast)
    A = np.array(A)
    B = np.array(B)

    return np.add(A, B)

def substracting_two_matrices(A, B):
    # This functions returns the result from substracting matrix B from matrix A

    # Make sure we have numpy matrices (type cast)
    A = np.array(A)
    B = np.array(B)

    return np.subtract(A, B)

# Tests
first_test_matrix = [4, 5]
second_test_matrix = [6, 5]

print(f"First matrix {first_test_matrix}")
print(f"Second matrix {second_test_matrix}")
print("Matrix Addition")
print(adding_two_matrices(first_test_matrix, second_test_matrix))
print("Matrix Substraction")
print(substracting_two_matrices(first_test_matrix, second_test_matrix))
