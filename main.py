from grid import Grid
from binary_tree import build_maze

rows = 8
cols = 8
newGrid = Grid(rows, cols)

build_maze(newGrid)

newGrid.print()
