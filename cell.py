class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.links = []

        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def neighbors(self):
        n = []

        self.north and n.append(self.north)
        self.south and n.append(self.south)
        self.east and n.append(self.east)
        self.west and n.append(self.west)

        return n

    def link(self, cell, bidirectional=True):
        self.links.append(cell)
        if bidirectional:
            cell.link(self, False)


    def unlink(self, cell, bidirectional=True):
        self.links.remove(cell)
        if bidirectional:
            cell.unlink(self, False)

    def isLinked(self, cell):
        isLinked = True if cell in self.links else False
        return isLinked
