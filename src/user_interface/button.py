from centeredtext import centeredtext


class Button:
	def __init__(self, pygame, area):
		self.pygame = pygame
		self.area = area

	def create(self, bgcolor, textcolor, bordercolor, left, top, width, height, text, action):

		box = self.pygame.Rect(
					left, 
					top, 
					width, 
					height
				)


		self.area.fill(bgcolor, box)

		test = centeredtext(text, left, top, width, height, self.pygame, textcolor)
		test.draw(self.area, bordercolor)