# function to create and prepopulate a list
# representing a sudoku problem
def sudoku_setup():
	lst = [[] for _ in range(9)]
	lst = [[4,0,0,0,0,2,8,0,9],
		   [0,2,0,1,0,0,0,0,0],
		   [0,0,5,0,0,0,6,0,0],
		   [7,0,0,0,3,0,0,0,0],
		   [0,3,0,2,1,8,0,7,0],
		   [0,0,0,0,9,0,0,0,8],
		   [0,0,4,0,0,0,7,0,0],
		   [0,0,0,0,0,7,0,6,0],
		   [1,0,6,4,0,0,0,0,3]]
	return lst2

# function to check the next empty position
# on the sudoku puzzle represented by a '0'
# sets current row and col to pos if found
def next_empty_pos(lst, pos):
	for row in range(9):
		for col in range(9):
			if (lst[row][col] == 0):
				pos[0] = row
				pos[1] = col
				return True
	return False

# function to check if numeber exist in
# all rows of the sudoku board
def row_check(lst, row, x):
	for i in range(9):
		if (lst[row][i] == x):
			return True
	return False

# function to check if number exist in
# all columns of the sudoku board
def col_check(lst, col, y):
	for i in range(9):
		if (lst[i][col] == y):
			return True
	return False

# function to check if number exist in
# 3x3 sudoku box
def box_check(lst, row, col, num):
	for i in range(3):
		for j in range(3):
			if (lst[i+row][j+col] == num):
				return True
	return False

# function that solves a given sudoku puzzle
def solve(lst):
	# current position on board
	pos = [0,0]
	# gets next empty pos, if no next empty pos, we are done
	if (not next_empty_pos(lst,pos)):
		return True
	# update current row / pos
	row = pos[0]
	col = pos[1]
	# try numbers 1-9 on current pos of board
	for i in range(1,10):
		# check for i occurence in row, col, and box
		if (not row_check(lst, row, i) and not col_check(lst, col, i) and not box_check(lst, row - row%3, col - col%3, i)):
			# make tenative assignment on current pos 
			lst[row][col] = i
			# recurse step to traverse the puzzle
			if (solve(lst)):
				return True
			# on back track, when failed, assign 0
			lst[row][col] = 0
	# back tracking step
	return False

if __name__ == "__main__":
	problem = sudoku_setup()
	if (solve(problem)):
		for i in problem:
			print(i)
	else:
		print("No solution.")