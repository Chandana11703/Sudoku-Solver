# N is the size of the 2D matrix N*N
N = 9

# Checks whether it will be legal to assign num to the given row, col
def isSafe(grid, row, col, num):
	for x in range(9):
		if grid[row][x] == num:
			return False

	for x in range(9):
		if grid[x][col] == num:
			return False

	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

# Takes a partially filled-in grid and attempts to assign values to all unassigned locations 
# Sudoku solution (non-duplication across rows,columns, and boxes) */

def solveSudoku(grid, row, col):
	
	if (row == N - 1 and col == N):
		return True
	
	if col == N:
		row += 1
		col = 0

	if grid[row][col] > 0:
		return solveSudoku(grid, row, col + 1)

	for num in range(1, N + 1, 1):
		if isSafe(grid, row, col, num):
		
			grid[row][col] = num

			if solveSudoku(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

