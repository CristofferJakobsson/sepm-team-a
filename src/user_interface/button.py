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

		buttonTextFont = self.pygame.font.Font('freesansbold.ttf', 28)
		pvcButtonRect = self.area.blit(
			buttonTextFont.render(
				centeredtext(text, left, top, width, height, self.pygame, textcolor), 
				True, 
				textcolor
			), 
			self.area.fill(
				bgcolor, 
				box
			)
		)

		self.pygame.draw.rect(self.area, bordercolor, box, 1)
