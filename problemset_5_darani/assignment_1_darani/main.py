from sparse_matrix import SparseMatrix

if __name__ == "__main__":
    sparse_matrix_A = SparseMatrix(3, 4)
    sparse_matrix_A[2, 3] = 5
    sparse_matrix_A[1, 2] = 12.3
    print(sparse_matrix_A)
    print(f"Vale at [2, 3] = {sparse_matrix_A[2, 3]}")
    print(f"Vale at [1, 1] = {sparse_matrix_A[1, 1]}")

    # region Test add
    print("\n\tTEST ADD")
    print("----------------")
    sparse_matrix_B = SparseMatrix(3, 4)
    sparse_matrix_B[2, 3] = 2
    sparse_matrix_B[1, 1] = 4
    print(sparse_matrix_A)
    print(sparse_matrix_B)
    print(sparse_matrix_A.add(sparse_matrix_B))
    # endregion

    # region Test sub
    print("\nTEST SUB")
    print("----------------")
    print(sparse_matrix_A)
    print(sparse_matrix_B)
    print(sparse_matrix_A.subtract(sparse_matrix_B))
    # endregion

    # region Test mult
    print("\nTEST MULT")
    print("----------------")
    sparse_matrix_A = SparseMatrix(4, 3)
    sparse_matrix_B = SparseMatrix(3, 6)
    sparse_matrix_A[1, 2] = 5
    sparse_matrix_A[2, 1] = 2
    sparse_matrix_A[0, 1] = 6
    sparse_matrix_B[2, 5] = 8
    sparse_matrix_B[2, 2] = 1
    sparse_matrix_B[0, 4] = 3
    sparse_matrix_B[1, 1] = 2
    print(sparse_matrix_A)
    print(sparse_matrix_B)
    print(sparse_matrix_A.multiply(sparse_matrix_B))
    # endregion

    # region Test transpose
    print("\nTEST TRANSPOSE")
    print("----------------")
    print(sparse_matrix_A)
    print(sparse_matrix_A.transpose())
    # endregion
