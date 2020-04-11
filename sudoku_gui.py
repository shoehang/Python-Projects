import pygame

class box():
	def __init__(self, x, y, width, height, color, text):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.text = text

	def getText(self):
		return self.text

	def setText(self, newText):
		self.text = newText

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))
		font = pygame.font.SysFont('comicsans', 30)
		text = font.render(self.text, 1, (0,0,0))
		canvas.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))

	def hover(self, pos):
		if (pos[0] > self.x and pos[0] < self.x + self.width):
			if (pos[1] > self.y and pos[1] < self.y + self.height):
				return True
		return False