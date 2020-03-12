from grid import Grid
from sidewinder import build_maze

rows = 10
cols = 10
newGrid = Grid(rows, cols)

build_maze(newGrid)

newGrid.print()
