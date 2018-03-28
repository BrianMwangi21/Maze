"""
Maze class
Holds the maze and initializes the starting point
"""
import os


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