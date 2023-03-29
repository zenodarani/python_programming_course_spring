from random import randint
from timeit import Timer
from typing import Type, Union
from matrix import Matrix
import matplotlib.pyplot as plt

from problemset_5_darani.assignment_1_darani.sparse_matrix import SparseMatrix


def _generate_random_matrix(matrix_type: Union[Type[Matrix], Type[SparseMatrix]], size: int):
    """
    Given a Matrix class (Matrix or SparseMatrix), creates an instance and initializes is with a few elements.
    """
    matrix = matrix_type(size, size)

    elements = size // 10 if size < 100 else 100

    for i in range(elements):
        i = randint(0, size-1)
        j = randint(0, size-1)

        while matrix[i, j] != 0:
            i = randint(0, size-1)
            j = randint(0, size-1)

        matrix[i, j] = randint(1, 100)
    return matrix


def sum_matrixes(collector_matrix, matrixes):
    """
    The test operation, given an empty matrix (collector_matrix) and a list of matrixes,
    collects the results of their sum in the collector matrix object.
    """
    for m in matrixes:
        collector_matrix += m


def run_experiment(matrix_type: Union[Type[Matrix], Type[SparseMatrix]], matrix_size: int, matrixes_number: int):
    """
    Runs the experiment for a given matrix class (Matrix or SparseMatrix).
    It is possible to provide the number of matrixes to be created, and the size of each.
    Returns the execution time in seconds.
    """

    matrixes = [_generate_random_matrix(matrix_type=matrix_type, size=matrix_size) for _ in range(matrixes_number)]
    collector_matrix = matrix_type(matrix_size, matrix_size)

    t = Timer(lambda: sum_matrixes(collector_matrix=collector_matrix, matrixes=matrixes))
    return t.timeit(number=1)


def main():

    matrix_sizes = [x for x in range(10, 1000, 100)]

    # run the experiment for the Sparse Matrix
    sparse_matrix_experiments = [run_experiment(matrix_type=SparseMatrix, matrix_size=size, matrixes_number=10) for size in matrix_sizes]
    print(f"Execution time: {sparse_matrix_experiments} s")

    # run the experiment for the Matrix
    matrix_experiment = [run_experiment(matrix_type=Matrix, matrix_size=size, matrixes_number=10) for size in matrix_sizes]
    print(f"Execution time: {matrix_experiment} s")

    # plots for the result
    plt.figure()
    # sparse matrix
    plt.plot(matrix_sizes, sparse_matrix_experiments, 'bo-', label='Sparse Matrix')
    # matrix
    plt.plot(matrix_sizes, matrix_experiment, 'ro-', label='Matrix')
    plt.ylabel('Time in seconds')
    plt.xlabel('Matrix size')
    plt.legend()
    plt.xticks(matrix_sizes, matrix_sizes)
    plt.grid(visible=True)
    plt.title("Sum of matrixes performance")
    plt.savefig('plot_sum_performance.png')



if __name__ == "__main__":
    main()
