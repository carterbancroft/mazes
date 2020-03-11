from grid import Grid
from binary_tree import build_maze

rows = 12
cols = 12
newGrid = Grid(rows, cols)

build_maze(newGrid)

newGrid.print()
