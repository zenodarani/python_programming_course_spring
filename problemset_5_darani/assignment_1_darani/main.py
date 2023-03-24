from sparse_matrix import SparseMatrix

if __name__ == "__main__":
    sparse_matrix_A = SparseMatrix(3, 4)
    sparse_matrix_A[2, 3] = 5
    sparse_matrix_A[1, 2] = 12.3
    print(sparse_matrix_A)
    print(f"Vale at [2, 3] = {sparse_matrix_A[2, 3]}")
