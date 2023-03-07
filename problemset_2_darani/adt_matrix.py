# Implementation of the Matrix ADT using a 2-D array.
from adt_array import Array2D


class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._theGrid = Array2D( numRows, numCols )
        self._theGrid.clear( 0 )

    # Returns the number of rows in the matrix.
    def numRows( self ):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols( self ):
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        self._theGrid[ ndxTuple[0], ndxTuple[1] ] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                self[ r, c ] *= scalar

    # Creates and returns a new matrix that is the transpose of this matrix.
    #def tranpose( self ):
    #......

    # Creates and returns a new matrix that results from matrix addition.
    def __add__( self, rhsMatrix ):
        assert Matrix._isSameSize(self, rhsMatrix), "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__( self, rhsMatrix ):
        assert Matrix._isSameSize(self, rhsMatrix), "Matrix sizes not compatible for the sub operation."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Subtract the corresponding elements in the two matrices.
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows() and self.numRows() == rhsMatrix.numCols(), \
            "Matrix sizes not compatible for the mul operation."
        # Create the new matrix
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        # Multiplication of rows with columns
        for r in range(newMatrix.numRows()):
            for c in range(newMatrix.numCols()):
                sum = 0
                for i in range(newMatrix.numRows()):
                    # multiplication of #n element of row with #n element of column
                    sum += self[r, i] * rhsMatrix[c, i]
                newMatrix[r, c] = sum
        return newMatrix

    # Returns a new matrix that is the transpose of this matrix
    def transpose(self):
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Transposition
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c ,r] = self[r, c]
        return newMatrix

    # Checks if two matrices are of the same size
    @staticmethod
    def _isSameSize(firstMatrix, secondMatrix):
        return firstMatrix.numRows() == secondMatrix.numRows() and \
            firstMatrix.numCols() == secondMatrix.numCols()

    def __str__(self):
        mtxStr = ''
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                mtxStr += f'{self[i, j]} '
            mtxStr += '\n'
        return mtxStr


def main():
    dataMtx1 = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
    dataMtx2 = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
    mtx1 = Matrix(3, 3)
    mtx2 = Matrix(3, 3)
    for i in range(mtx1.numRows()):
        for j in range(mtx1.numCols()):
            mtx1[i, j] = dataMtx1[i][j]
    for i in range(mtx2.numRows()):
        for j in range(mtx2.numCols()):
            mtx2[i, j] = dataMtx2[i][j]
    print('Matrix 1:')
    print(mtx1)
    print('Matrix 2:')
    print(mtx2)
    print('Subtraction:')
    print(mtx1 - mtx2)
    print('Multiplication:')
    print(mtx1 * mtx2)
    print('Transpose of mtx 1:')
    print(mtx1.transpose())


main()
