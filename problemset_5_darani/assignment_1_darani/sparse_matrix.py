from __future__ import annotations
from email import message
# allows typing using the class you are defining
from typing import Optional, Tuple


class SparseMatrix:
    # Create a sparse matrix of
    def __init__(self, rows: int, cols: int):
        if rows <= 0:
            raise SparseMatrixException("Rows must be > 0!")
        elif cols <= 0:
            raise SparseMatrixException("Columns must be > 0!")

        self._rows = rows
        self._cols = cols
        self._elements = list()  # a dynamic list is needed

    # Return the number of rows
    def rows(self) -> int:
        return self._rows

    # Return the number of columns in
    def cols(self) -> int:
        return self._cols

    # Helper method used to find a specific matrix element (row,col) in the
    # list of non-zero entries. None is returned if the element is not found.
    def _find_position(self, row: int, col: int) -> Optional[int]:
        for i, e in enumerate(self._elements):
            if row == e.row and col == e.col:
                return i  # return the index of the element if found.
        return None  # return None when the element is zero.

    # Set the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, position: Tuple[int, int], value: float):

        # find the element
        index = self._find_position(position[0], position[1])

        # if the element is NOT found in the list.
        if index is None:
            # zero is considered an empty element
            if value == 0:
                return

            element = _MatrixElement(position[0], position[1], value)
            self._elements.append(element)
            return
        else:  # the element is found in the list!
            if value == 0:
                self._elements.pop(index)
                return

            self._elements[index].value = value

    def __str__(self):
        string_repr = ""
        for i in range(self._rows):
            for j in range(self._cols):
                string_repr += f"{self[i, j]}\t"
            string_repr += "\n"
        return string_repr

    def __repr__(self) -> str:
        return self.__str__()

    # *** ASSIGNMENT 1.2 ****************************************************************************************
    # Return the value of element (i,j) of the matrix: x[i,j]
    def __getitem__(self, coordinates: Tuple[int, int]) -> float:
        if coordinates[0] >= self._rows or coordinates[0] < 0:
            raise SparseMatrixException(
                f"Index of row out of bound for index={coordinates[0]} and {self._rows} rows")
        if coordinates[1] >= self._cols or coordinates[1] < 0:
            raise SparseMatrixException(
                f"Index of col out of bound for index={coordinates[1]} and {self._cols} cols")
        for element in self._elements:
            if element.row == coordinates[0] and element.col == coordinates[1]:
                return element.value
        return 0

    def add(self, o: SparseMatrix) -> SparseMatrix:
        if not (self._rows == o._rows and self._cols == o._cols):
            raise SparseMatrixException("Invalid other matrix size")
        result_matrix = SparseMatrix(self._rows, self._cols)
        for element in self._elements:
            result_matrix[element.row, element.col] = element.value + o[element.row, element.col]
        # the other values that are zero in self but non-zero in o
        for element in o._elements:
            if self[element.row, element.col] == 0:
                result_matrix[element.row, element.col] = element.value
        return result_matrix

    def subtract(self, o: SparseMatrix) -> SparseMatrix:
        ... # TODO implement

    def multiply(self, o: SparseMatrix) -> SparseMatrix:
        ... # TODO implement

    def transpose(self) -> SparseMatrix:
        ... # TODO implement

    # *** ASSIGNMENT 1.3 ****************************************************************************************
    def __add__(self, o: SparseMatrix):
        ... # TODO implement

    def __mul__(self, o: SparseMatrix):
        ... # TODO implement

    def __sub__(self, o: SparseMatrix):
        ... # TODO implement


# Storage class for holding the non-zero matrix elements.
class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


# simple custom Exception to manage errors
class SparseMatrixException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        return self._message
    
    def __repr__(self) -> str:
        return self._message
