from grid import Grid

rows = 3
cols = 3
newGrid = Grid(rows, cols)


for cell in newGrid.each_cell():
    print(cell)

cell = newGrid[0, 0]
cell.link(cell.south)
cell.link(cell.east)
print(cell.isLinked(cell.south))
cell.unlink(cell.south)
print(len(cell.links))
print(cell.isLinked(cell.south))
print(cell.isLinked(cell.east))
#print(len(cell.neighbors()))

print(newGrid.random_cell())
