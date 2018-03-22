# Maze solver in Python
import os
import time


class Point(object):
    row, col = 0, 0

    def __init__(self):
        self.row = 0
        self.col = 0

    def init_as_coords(self, row, col):
        self.row = row
        self.col = col

    def init_as_point(self, point):
        self.row = point.row
        self.col = point.col

    def __repr__(self):
        return "[%s,%s]" % (self.row, self.col)


class Maze(object):
    maze = None
    maze_data = []
    row_limit, col_limit = 0, 0

    def __init__(self):
        #   First check the file for the maze
        if os.path.isfile("maze.txt"):
            with open("maze.txt") as file:
                for line in file:
                    single_line_data = list(line)

                    for s_d in range(0, len(single_line_data)):
                        if single_line_data[s_d] != "\n":
                            self.maze_data.append(single_line_data[s_d])
                        else:
                            self.col_limit = s_d

                    self.row_limit += 1

            # With the limit height and length, we can init the 2d maze array
            self.maze = [[0 for x in range(self.col_limit)] for y in range(self.row_limit)]

            data_counter = 0
            for row in range(0, self.row_limit):
                for col in range(0, self.col_limit):
                    self.maze[row][col] = self.maze_data[data_counter]
                    data_counter += 1
        else:
            print("Maze.txt does not exist")

    def print_maze(self):
        print("\nMaze >> ")
        for row in range(0, self.row_limit):
            print(''.join(self.maze[row]))


class Solver(object):
    maze_to_solve = Maze()
    start_point, current_point, previous_point = Point(), Point(), Point()

    def __init__(self, maze_object):
        self.maze_to_solve = maze_object

        # Initialize required coordinates
        self.get_start_and_end()
        self.current_point.init_as_point(self.start_point)
        self.previous_point.init_as_point(self.start_point)

        # Now solve
        self.maze_to_solve.print_maze()
        self.solve_maze()
        print("Maze is done")

    def get_start_and_end(self):
        for row in range(0, self.maze_to_solve.row_limit):
            for col in range(0, self.maze_to_solve.col_limit):
                if self.maze_to_solve.maze[row][col] == "S":
                    self.start_point.init_as_coords(row, col)
                    break

    def solve_maze(self):
        while True:
            # First get all possible points to move
            all_possible_moves = self.next_empty_points(self.current_point)

            # Then remove all the previous points from possible moves
            final_possible_moves = []
            for pos_p in range(0, len(all_possible_moves)):
                if all_possible_moves[pos_p].row == self.previous_point.row and all_possible_moves[pos_p].col == self.previous_point.col:
                    pass
                else:
                    final_possible_moves.append(all_possible_moves[pos_p])

            print("Next points                : " + str(final_possible_moves))

            # Loop through the solutions
            if len(final_possible_moves) == 1:
                # Move the Solver to the next point
                self.maze_to_solve.maze[final_possible_moves[0].row][final_possible_moves[0].col] = "S"

                # Make the previous point to be the current point, then make the current point to be the next point
                self.previous_point.init_as_point(self.current_point)
                self.current_point.init_as_coords(final_possible_moves[0].row, final_possible_moves[0].col)

                print("Current to become previous : " + str(self.previous_point))
                print("Next to become current     : " + str(self.current_point))

                self.maze_to_solve.print_maze()
            else:
                print("Breaking")
                break

    def next_empty_points(self, point):
        all_empty_points = []

        if self.maze_to_solve.maze[point.row][point.col + 1] == " ":
            # To the right
            right_point = Point()
            right_point.init_as_coords(point.row, point.col + 1)
            all_empty_points.append(right_point)

        if self.maze_to_solve.maze[point.row][point.col - 1] == " ":
            # To the left
            left_point = Point()
            left_point.init_as_coords(point.row, point.col - 1)
            all_empty_points.append(left_point)

        if self.maze_to_solve.maze[point.row + 1][point.col] == " ":
            # To the south
            south_point = Point()
            south_point.init_as_coords(point.row + 1, point.col)
            all_empty_points.append(south_point)

        if self.maze_to_solve.maze[point.row - 1][point.col] == " ":
            # To the north
            north_point = Point()
            north_point.init_as_coords(point.row - 1, point.col)
            all_empty_points.append(north_point)

        return all_empty_points

    def print_stats(self):
        self.maze_to_solve.print_maze()
        print("Start Point   : " + str(self.start_point))
        print("Current Point : " + str(self.current_point))


# Create new Maze Object
maze = Maze()
solver = Solver(maze)
