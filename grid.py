import random
from cell import Cell


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._grid = [[None for col in range(cols)] for row in range(rows)]

        self._prepare_grid()
        self._configure_cells()

    def _prepare_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self._grid[row][col] = Cell(row, col)

    def _configure_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self[row, col]

                cell.north = self[row - 1, col]
                cell.south = self[row + 1, col]
                cell.west = self[row, col - 1]
                cell.east = self[row, col + 1]

    def __getitem__(self, tup):
        row, col = tup

        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.cols:
            return None

        return self._grid[row][col]

    def random_cell(self):
        row = random.randrange(self.rows - 1)
        col = random.randrange(self.cols - 1)

        return self[row, col]

    def size(self):
        return self.rows * self.cols
