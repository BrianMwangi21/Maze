# Maze solver in Python
from packages.maze import Maze
from packages.solver import Solver

# Create new Maze Object
if __name__ == "__main__":
    maze = Maze()
    solver = Solver(maze, "S", True)
    solver.solve_maze()
    solver.print_route()
    solver.get_route_branches()
