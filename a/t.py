import queue

def mazeEnd(maze, path):
	for row in maze:
		for pos in row:
			if pos == 'S':
				start == row.index(pos)

	

if __name__ == '__main__':
	grid = [['S', ' ', ' ', ' ', ' ', ' '],
			[' ', '#', ' ', ' ', '#', ' '],
			[' ', ' ', '#', ' ', '#', ' '],
			[' ', ' ', ' ', '#', ' ', ' '],
			[' ', ' ', ' ', ' ', '#', ' '],
			[' ', ' ', ' ', ' ', ' ', 'E']]
	print(grid)
