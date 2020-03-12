import random

def build_maze(grid):
    for row in grid:
        run = []

        for cell in row:
            run.append(cell)

            at_eastern_boundary = cell.east == None
            at_northern_boundary = cell.north == None

            # Heads or tails (0 or 1)
            # Heads link east, tails close the run (if possible)
            rand = random.choice(range(2))

            # We should close the run if we've reached the eastern edge of the
            # grid, or if we've flipped tails and we're not on the northern row.
            should_close_out = (
                at_eastern_boundary 
                or (not at_northern_boundary and rand == 1)
            )

            if should_close_out:
                randCell = random.choice(run)

                if randCell.north:
                    randCell.link(randCell.north)

                run.clear()
            else:
                cell.link(cell.east)
