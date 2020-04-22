from sudoku_gui import *
import sys

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
	boxes = [[] for _ in range(9)]
	for i in range(len(lst)):
		for j in range(len(lst)):
			num = box(10 + (i * 30), 10 + (j * 30), 28, 28, (255,255,255), lst[i][j])
			boxes[i].append(num)
	return boxes

# function to check the next empty position
# on the sudoku puzzle represented by a '0'
# sets current row and col to pos if found
def next_empty_pos(lst, pos):
	for row in range(9):
		for col in range(9):
			currBox = lst[row][col]
			if (currBox.getNum() == 0):
				pos[0] = row
				pos[1] = col
				return True
	return False

# function to check if numeber exist in
# all rows of the sudoku board
def row_check(lst, row, x):
	for i in range(9):
		currBox = lst[row][i]
		if (currBox.getNum() == x):
			return True
	return False

# function to check if number exist in
# all columns of the sudoku board
def col_check(lst, col, y):
	for i in range(9):
		currBox = lst[i][col]
		if (currBox.getNum() == y):
			return True
	return False

# function to check if number exist in
# 3x3 sudoku box
def box_check(lst, row, col, num):
	for i in range(3):
		for j in range(3):
			currBox = lst[i+row][i+col]
			if (currBox.getNum() == num):
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
			currBox = lst[row][col]
			currBox.setNum(i)
			# recurse step to traverse the puzzle
			if (solve(lst)):
				return True
			# on back track, when failed, assign 0
			currBox.setNum(0)
	# back tracking step
	return False

if __name__ == "__main__":
	pygame.init()

	WHITE = (255, 255, 255)
	LIGHTGRAY = (200, 200, 200)
	BLACK = (0, 0, 0)
	WIDTH = 600
	HEIGHT = 400

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Sudoku')
	CANVAS.fill(LIGHTGRAY)

	SOLVEBUTTON = box(300, 300, 90, 60, WHITE, 'Solve')
	problem = sudoku_setup()

	while True:
		for row in problem:
			for col in row:
				col.draw(CANVAS)

		SOLVEBUTTON.draw(CANVAS)
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			if (event.type == pygame.MOUSEMOTION):
				if (SOLVEBUTTON.hover(pos)):
					SOLVEBUTTON.color = (225,225,225)
				else:
					SOLVEBUTTON.color = WHITE
			if (event.type == pygame.MOUSEBUTTONDOWN):
				if (SOLVEBUTTON.hover(pos)):
					solve(problem)
		pygame.display.update()