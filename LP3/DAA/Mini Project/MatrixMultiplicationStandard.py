import numpy as np
import time


def matrix_multiply(A, B):
    # Get the number of rows and columns
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    # Initialize the result matrix
    result = np.zeros((rows_A, cols_B))

    # Perform standard matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


import threading


def multiply_row(A, B, result, row):
    rows_B, cols_B = B.shape
    for j in range(cols_B):
        for k in range(A.shape[1]):
            result[row][j] += A[row][k] * B[k][j]


def multithreaded_matrix_multiply_row(A, B):
    rows_A = A.shape[0]
    cols_B = B.shape[1]
    result = np.zeros((rows_A, cols_B))

    threads = []
    for i in range(rows_A):
        thread = threading.Thread(target=multiply_row, args=(A, B, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


def multiply_cell(A, B, result, row, col):
    for k in range(A.shape[1]):
        result[row][col] += A[row][k] * B[k][col]


def multithreaded_matrix_multiply_cell(A, B):
    rows_A, cols_B = A.shape[0], B.shape[1]
    result = np.zeros((rows_A, cols_B))

    threads = []
    for i in range(rows_A):
        for j in range(cols_B):
            thread = threading.Thread(target=multiply_cell, args=(A, B, result, i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result
def performance_analysis():
    # Create two random matrices
    size = 100  # You can change this size for performance testing
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # Standard matrix multiplication
    start_time = time.time()
    result_standard = matrix_multiply(A, B)
    standard_time = time.time() - start_time
    print(f"Standard Matrix Multiplication Time: {standard_time:.4f} seconds")

    # Multithreaded matrix multiplication (one thread per row)
    start_time = time.time()
    result_threaded_row = multithreaded_matrix_multiply_row(A, B)
    threaded_row_time = time.time() - start_time
    print(f"Multithreaded Matrix Multiplication (Row) Time: {threaded_row_time:.4f} seconds")

    # Multithreaded matrix multiplication (one thread per cell)
    start_time = time.time()
    result_threaded_cell = multithreaded_matrix_multiply_cell(A, B)
    threaded_cell_time = time.time() - start_time
    print(f"Multithreaded Matrix Multiplication (Cell) Time: {threaded_cell_time:.4f} seconds")

# Run the performance analysis
performance_analysis()
