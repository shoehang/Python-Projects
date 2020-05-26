import sys
import pygame

#elementary box clss w draw method
class box():
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color

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
	for row in range(len(grid)):
		for col in range(len(grid)):
			gridBox = box(2 + (row * 20), 2 + (col * 20), 19, 19, (255, 255, 255))
			grid[row].append(gridBox)
	return grid

def redraw(grid, canvas):
	for row in grid:
		for col in row:
			col.draw(canvas)

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
				print("clicked")
				for row in GRID:
					for col in row:
						if (col.hover(pos)):
							col.color = BLACK
		pygame.display.update()