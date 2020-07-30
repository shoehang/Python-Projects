import queue

def mazeEnd(maze, path):
	start = 0

	for row in maze:
		for pos in row:
			if pos == 'S':
				start == row.index(pos)
	
	return start

if __name__ == '__main__':
	grid = [['S', ' ', ' ', ' ', ' ', ' '],
			[' ', '#', ' ', ' ', '#', ' '],
			[' ', ' ', '#', ' ', '#', ' '],
			[' ', ' ', ' ', '#', ' ', ' '],
			[' ', ' ', ' ', ' ', '#', ' '],
			[' ', ' ', ' ', ' ', ' ', 'E']]

	# new queue
	pathQueue = queue.Queue()
	# start at empty path
	pathQueue.put("")
	# placeholder
	currentPath = ""

	# check to see path leads to exit
	while not mazeEnd(grid, currentPath):
		# if not, grab from queue and add UDLR moves
		currentPath = pathQueue.get()
		for direction in ["U", "D", "L", "R"]:
			newPath = currentPath + direction
			# check validity of newPath, and add to queue
			if valid(gric, newPath):
				pathQueue.put(newPath)

	print(mazeEnd)
