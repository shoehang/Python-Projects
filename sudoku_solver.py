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
	return lst

# function to check the next empty position
# on the sudoku puzzle represented by a '0'
# sets current row and col to pos if found
def next_empty_pos(lst, row, col):
	for i in range(9):
		for j in range(9):
			if (lst[i][j] == 0):
				row = i
				col = j
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
		if (lst[i][col] == x):
			return True
	return False

def solve_puzzle(lst):
	# current position on board
	row = 0
	col = 0

	if (not next_empty_pos(lst,row,col)):
		return True

	for i in range(1,10):
		

if __name__ == "__main__":
	print(sudoku_setup())