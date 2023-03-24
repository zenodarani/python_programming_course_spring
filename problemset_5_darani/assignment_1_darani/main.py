from sparse_matrix import SparseMatrix

if __name__ == "__main__":
    sparse_matrix_A = SparseMatrix(3, 4)
    sparse_matrix_A[2, 3] = 5
    sparse_matrix_A[1, 2] = 12.3
    print(sparse_matrix_A)
    print(f"Vale at [2, 3] = {sparse_matrix_A[2, 3]}")
    print(f"Vale at [1, 1] = {sparse_matrix_A[1, 1]}")

    # test add
    sparse_matrix_B = SparseMatrix(3, 4)
    sparse_matrix_B[2, 3] = 2
    sparse_matrix_B[1, 1] = 4
    print(sparse_matrix_A)
    print("-----")
    print(sparse_matrix_B)
    print("-----")
    print(sparse_matrix_A.add(sparse_matrix_B))

    # test sub
    print()
    print(sparse_matrix_A)
    print("-----")
    print(sparse_matrix_B)
    print("-----")
    print(sparse_matrix_A.subtract(sparse_matrix_B))

