import sys
import pygame

#elementary box clss w draw method
class box():
	def __init__(self, x, y, width, height, text, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.color = color

	def getPos(self):
		return (self.x, self.y)

	def getText(self):
		return self.text

	def setText(self, newText):
		self.text = newText

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))
		if not(self.text == " " or self.text == "#" or self.text == "S" or self.text == "E"):
			font = pygame.font.SysFont('comicsans', 25)
			text = font.render(str(self.text), 1, (0,0,0))
			canvas.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))
		
	def hover(self, pos):
		if (pos[0] > self.x and pos[0] < self.x + self.width):
			if (pos[1] > self.y and pos[1] < self.y + self.height):
				return True
		return False

# boxes etc
def setup():
	grid = [[] for _ in range(22)]
	for col in range(len(grid)):
		for row in range(len(grid)):
			gridBox = box(2 + (row * 20), 2 + (col * 20), 19, 19, " ", (255, 255, 255))
			grid[col].append(gridBox)
	return grid

def redraw(grid, canvas):
	for row in grid:
		for col in row:
			col.draw(canvas)

def getMazeArray(grid):
	mazeArray = []
	for i in grid:
		row = []
		for j in i:
			row.append(j.getText())
		mazeArray.append(row)
	return mazeArray
		

if __name__ == '__main__':
	pygame.init()

	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	WIDTH = 443
	HEIGHT = 475

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('WIP algo')
	CANVAS.fill(BLACK)

	GRID = setup()
	SOLVEBUTTON = box(2, 446, 100, 25, 'Find', WHITE)
	RESETBUTTON = box(106, 446, 100, 25, 'Reset', WHITE)

	while True:
		redraw(GRID, CANVAS)
		SOLVEBUTTON.draw(CANVAS)
		RESETBUTTON.draw(CANVAS)

		# pos of mouse on pygame window
		pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			# mousclick on:
			if (event.type == pygame.MOUSEBUTTONDOWN):
				# find
				if (SOLVEBUTTON.hover(pos)):
					print(getMazeArray(GRID))
					print("finding")
				# reset
				if (RESETBUTTON.hover(pos)):
					GRID = setup()
					print("resetting")
				# mazeblocks
				for row in GRID:
					for col in row:
						if (col.hover(pos)):
							if (col.getText() == " "):
								col.setText("#")
								col.color = BLACK
							else:
								col.setText(" ")
								col.color = WHITE
			# key presses
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_s):
					for row in GRID:
						for col in row:
							if (col.hover(pos)):
								col.setText("S")
								col.color = GREEN
				if (event.key == pygame.K_e):
					for row in GRID:
						for col in row:
							if (col.hover(pos)):
								col.setText("E")
								col.color = RED
		pygame.display.update()