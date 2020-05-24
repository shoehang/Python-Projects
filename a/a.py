import sys
import pygame

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

def setup():
	grid = [[] for _ in range(9)]

if __name__ == '__main__':
	pygame.init()

	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	WIDTH = 400
	HEIGHT = 450

	CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('WIP algo')
	CANVAS.fill(BLACK)

	while True:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			if (event.type == pygame.MOUSEBUTTONDOWN):
				print("clicked")
		pygame.display.update()