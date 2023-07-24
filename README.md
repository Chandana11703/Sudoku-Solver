# Sudoku-Solver
The game has been built using a neat UI, where the client sends the unsolved sudoku to the server from which the server analyzes and gives back the feasible solution.
All of this has been done by integrating the concepts of Computer Networks using Python.
To execute this run the server which is named as SudokuSolver using command 'python SudokuSolver.py'.
Now the server will wait for connections. Open a new terminal and execute cient using command 'Python client.py'.
After executing this, a connection will be established between client and server using the IP address and immediately a GUI opens asking client to enter an unsolved sudoku.
When client enters unsolved sudoku the Solver will analyze the solution but wait for the client to solve it.
If client is unable to solve the sudoku , the client can click on solution which gives Solution of the unsolved Sudoku
