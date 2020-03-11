import random

def build_maze(grid):
    for cell in grid.each_cell():
        neighbors = []
        if cell.north:
            neighbors.append(cell.north)
        if cell.east:
            neighbors.append(cell.east)

        if len(neighbors) == 0:
            continue

        neighbor = random.choice(neighbors)
        if neighbor:
            cell.link(neighbor)
