# Implements the LifeGrid ADT for use with the game of Life.
import copy
from adt_array import Array2D


class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        # Allocate the 2-D array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cells to dead.
        self.configure(list())

    # Returns the number of rows in the grid.
    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure(self, coordList):
        # Clear the game grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Returns the number of live neighbors for the given cell.
    def numLiveNeighbors( self, row, col):
        startRow = row - 1 if row - 1 >= 0 else row
        startCol = col - 1 if col - 1 >= 0 else col
        endRow = row + 1 if row + 1 < self.numRows() else row
        endCol = col + 1 if col + 1 < self.numCols() else col
        numAliveCells = 0
        for i in range(startRow, endRow + 1):
            for j in range(startCol, endCol + 1):
                if not(i == row and j == col) and self.isLiveCell(i, j):
                    numAliveCells += 1
        return numAliveCells

    # Evolve the game to a given number of generations
    def evolve(self, generations=1):
        for gen in range(generations):
            nextLifeGrid = LifeGrid(self.numRows(), self.numCols())
            for row in range(self.numRows()):
                for col in range(self.numCols()):
                    numLive = self.numLiveNeighbors(row, col)
                    if (self.isLiveCell(row, col) and 2 <= numLive <= 3) or \
                            (not self.isLiveCell(row, col) and numLive == 3):
                        # Change the gridstatus of the next generation
                        nextLifeGrid.setCell(row, col)
            self._grid = nextLifeGrid._grid


GRID_ROWS = 15
GRID_COLS = 15
DEFAULT_GENS = 9
CONF_1 = [(5, 5), (4, 6), (3, 7)]
CONF_2 = [(7, 7), (8, 8), (9, 9), (10, 10), (11, 11),
          (11, 7), (10, 8), (9, 9), (8, 10), (7, 11)]
CONF_3 = [(3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
          (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
          (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
          (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
          (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
CONF_4 = [(1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
          (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
          (5, 3), (5, 7)]
CONF_5 = [(3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
          (5, 6), (5, 7), (5, 9), (5, 10)]
CONF_6 = [(3, 3), (3, 4), (4, 4),
          (3, 6), (3, 7), (4, 6),
          (6, 4), (7, 4), (7, 3),
          (6, 6), (7, 6), (7, 7)]
CONF_7 = [(0, 0), (0, 1), (1, 0),
          (1, 2), (3, 2),
          (3, 4), (5, 4),
          (5, 6), (7, 6),
          (7, 8), (9, 8),
          (9, 10), (11, 10),
          (11, 12), (12, 11), (12, 12)]


def draw(lifeGrid):
    for i in range(lifeGrid.numRows()):
        for j in range(lifeGrid.numCols()):
            print('#', end=' ') if lifeGrid.isLiveCell(i, j) else print('.', end=' ')
        print('')


# Play the game of life
def play(lifegrid, generations):
    print('\nGeneration 1')
    draw(lifegrid)
    for i in range(generations):
        lifegrid.evolve()
        print(f'\nGeneration {i + 2}')
        draw(lifegrid)


def main():
    grid = LifeGrid(GRID_ROWS, GRID_COLS)

    print('--- CONF_1 ---')
    grid.configure(CONF_1)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_2 ---')
    grid.configure(CONF_2)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_3 ---')
    grid.configure(CONF_3)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_4 ---')
    grid.configure(CONF_4)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_5 ---')
    grid.configure(CONF_5)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_6 ---')
    grid.configure(CONF_6)
    play(grid, DEFAULT_GENS)
    print('\n--- CONF_7 ---')
    grid.configure(CONF_7)
    play(grid, DEFAULT_GENS)


main()
