"""
Point class.
Holds the row and col values of the maze
"""


class Point(object):
    row, col = 0, 0

    def __init__(self):
        self.row = 0
        self.col = 0

    def init_as_coords(self, row: int, col: int):
        self.row = row
        self.col = col

    def init_as_point(self, point):
        self.row = point.row
        self.col = point.col

    def __repr__(self):
        return "[%s,%s]" % (self.row, self.col)