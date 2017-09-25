import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


class Playernames: 
	def __init__(self, screen):
		self.screen = screen
	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, message):
		"Print a message in a box in the middle of the screen"
		fontobject = pygame.font.Font(None,30)
		pygame.draw.rect(self.screen, (247, 247, 247),
										 ((self.screen.get_width() / 2) - 200,
											(self.screen.get_height() / 2) - 25,
											400,50), 0)
		pygame.draw.rect(self.screen, (144, 148, 150),
										 ((self.screen.get_width() / 2) - 202,
											(self.screen.get_height() / 2) - 26,
											402,52), 1)
		if len(message) != 0:
			self.screen.blit(fontobject.render(message, 1, (74, 74, 74)),
									((self.screen.get_width() / 2) - 200, (self.screen.get_height() / 2) - 25))
		pygame.display.flip()

	def ask(self, question):
		"ask(screen, question) -> answer"
		pygame.font.init()
		current_string = []
		self.display_box(question + ": " + "".join(current_string))
		while 1:
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				break
			elif inkey == K_MINUS:
				current_string.append("_")
			elif inkey <= 127:
				current_string.append(chr(inkey))
			self.display_box(question + ": " + "".join(current_string))
		return "".join(current_string)



# def main():
# 	screen = pygame.display.set_mode((320,240))
# 	pn = Playernames(screen)
# 	pn.askfor(8)


# if __name__ == '__main__': main()