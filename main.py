# Maze solver in Python
import argparse
from packages.maze import Maze
from packages.solver import Solver

parser = argparse.ArgumentParser()
parser.add_argument("letter", help="This is the initial letter to use")
parser.add_argument("--trail", help="This sets the trail to true", action="store_true")
args = parser.parse_args()

if __name__ == "__main__":
    # Create new Maze Object
    maze = Maze()

    if args.trail:
        solver = Solver(maze, args.letter, True, [] )
    else:
        solver = Solver(maze, args.letter, False, [] )

    solver.solve_maze()
    solver.print_routes()
    solver.get_shortest_route()
