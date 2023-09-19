def matrix_multiply(A, B):
    """
    Performs matrix multiplication of two matrices A and B.

    Args:
        A (list of list of int/float): A 2D list representing matrix A.
        B (list of list of int/float): A 2D list representing matrix B.

    Raises:
        ValueError: If the number of columns in A is not equal to the number of rows in B.

    Returns:
        list of list of int/float: A 2D list representing the result of the matrix multiplication.
    """



    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to number of rows in B.")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[2, 0], [1, 3]]
    result = matrix_multiply(A, B)
    for row in result:
        print(row)
