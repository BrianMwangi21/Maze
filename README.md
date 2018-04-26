# Maze Solver

Edit 1:

The solver now identifies the end of the maze and only saves the routes that actually get there.
It then shows the shortest route that can be used.
Now also has command line commands for launch i.e.
```
$ python main.py S --trail

// S :- is the letter which in the maze identifies the start
// --trail :- adds a trail while printing maze. leaving it empty will only show the last points of the solvers
```

Edit 0:

This is a simple implementation of a Maze Solver in Python.

The Maze itself is made in the text file `maze.txt` and represented as a 2D array in the program.
The program the searches for the start which is represented by the letter 'S' in the file itself.

A Solver object then goes through the maze trying to find the end.
It finds the next empty cell and moves towards it until it gets to a junction with > 1 options.
At the junction, the initial solver creates child solvers which move on in each of the available options.

For now, their is no common end, just dead-ends. When the child solvers get to a dead end, they stop. The loop
continues until all dead-ends are reached.
