from centeredtext import centeredtext


class Button:
	def __init__(self, pygame, area):
		self.pygame = pygame
		self.area = area

	def create(self, bgcolor, textcolor, bordercolor, left, top, width, height, text, action):

		self.box = self.pygame.Rect(
					left, 
					top, 
					width, 
					height
				)

		self.action = action
		self.area.fill(bgcolor, self.box)
		self.text = text
		test = centeredtext(text, left, top, width, height, self.pygame, 28, textcolor)
		test.draw(self.area, bordercolor)
		return self