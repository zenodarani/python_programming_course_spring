from __future__ import annotations
from typing import Tuple  # allows typing using the class you are defining


class Matrix:

    def __init__(self, rows: int, cols: int):
        if rows <= 0:
            raise MatrixException("Rows must be > 0!")
        elif cols <= 0:
            raise MatrixException("Columns must be > 0!")

        self._rows = rows
        self._cols = cols
        self._matrix = [[0] * cols for _ in range(rows)]

    def rows(self) -> int:
        return self._rows

    def cols(self) -> int:
        return self._cols

    def __getitem__(self, coordinates: Tuple[int, int]):
        return self._matrix[coordinates[0]][coordinates[1]]

    def __setitem__(self, coordinates: Tuple[int, int], value: float):
        self._matrix[coordinates[0]][coordinates[1]] = value

    def scale_by(self, scalar: float):
        for r in range(self.rows()):
            for c in range(self.cols()):
                self[r, c] *= scalar

    def __add__(self, o: Matrix):
        if self._rows != o._rows or self._cols != o._cols:
            raise MatrixException("Matrix sizes incompatible!")

        new_matrix = Matrix(self.rows(), self.cols())

        for r in range(self.rows()):
            for c in range(self.cols()):
                new_matrix[r, c] = self[r, c] + o[r, c]
        return new_matrix

    def __sub__(self, o: Matrix):
        if self._rows != o._rows or self._cols != o._cols:
            raise MatrixException("Matrix sizes incompatible!")

        new_matrix = Matrix(self.rows(), self.cols())

        for r in range(self.rows()):
            for c in range(self.cols()):
                new_matrix[r, c] = self[r, c] - o[r, c]

        return new_matrix

    def __mul__(self, o: Matrix):
        if self._cols != o._rows:
            raise MatrixException("Lefthand matrix column must equal righthand matrix row size.")

        new_matrix = Matrix(self.rows(), o.numCols())

        for i in range(self.rows()):
            for j in range(o.numCols()):
                for k in range(o.numRows()):
                    new_matrix[i, j] += self[i, k] * o[k, j]

        return new_matrix


class MatrixException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self._message = message

    def __str__(self) -> str:
        return self._message

    def __repr__(self) -> str:
        return self._message
