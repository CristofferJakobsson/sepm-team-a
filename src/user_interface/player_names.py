import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


class Playernames:
	"""
	Playernames encapsulates an area of the screen asking for player name input and providing an input box for players to provide their chosen name.
	"""
	def __init__(self, screen):
		"""
		Construct a new Playernames object.

		:param self: A reference to the Playernames object itself
		:return: returns nothing
		"""
		self.screen = screen
	def get_key(self):
		"""
		Gets the key input from the keyboard.

		:param self: A reference to the Playernames object itself
		:return: returns nothing
		"""
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, message):
		"""
		Displays a box on the screen with a given message.

		:param self: A reference to the Playernames object itself
		:param message: The message to be displayed within the box
		:return: returns nothing
		"""
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

	def ask(self, question, previousanswers=[]):
		"""
		Asks the player a question and expects an input in the form of key-presses on the keyboard

		:param self: A reference to the Playernames object itself
		:param question: The question asked of the player
		:return: returns nothing
		"""
		"ask(screen, question) -> answer"
		pygame.font.init()
		current_string = []
		self.display_box(question + ": " + "".join(current_string))
		while 1:
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				if (not len([s for s in previousanswers if s=="".join(current_string)])>0):
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