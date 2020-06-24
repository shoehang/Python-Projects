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

def printText(grid):
	for i in grid:
		row = []
		for j in i:
			row.append(j.getText())
		print(row)

if __name__ == '__main__':
	pygame.init()

	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	WIDTH = 443
	HEIGHT = 450

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('WIP algo')
	CANVAS.fill(BLACK)

	GRID = setup()

	while True:
		redraw(GRID, CANVAS)

		pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			if (event.type == pygame.MOUSEBUTTONDOWN):
				for row in GRID:
					for col in row:
						if (col.hover(pos)):
							if (col.getText() == " "):
								col.setText("#")
								col.color = BLACK
							else:
								col.setText(" ")
								col.color = WHITE
							printText(GRID)
		pygame.display.update()