from centeredtext import centeredtext


class Button:
	"""
	Button encapsulates a pygame and a clickable area which invokes a given action.
	"""
	def __init__(self, pygame, area):
		"""
		Construct a new Button object.

		:param self: A reference to the Button object itself
		:param pygame: The pygame instance running
		:param area: The area on which to draw on
		:return: returns nothing
		"""
		self.pygame = pygame
		self.area = area

	def create(self, bgcolor, textcolor, bordercolor, left, top, width, height, text, action):
		"""
		Draw a new Button object on the screen.

		:param self: A reference to the Button object itself
		:param bgcolor: The background color of the Button
		:param textcolor: The text color of the Button
		:param bordercolor: The border color of the Button
		:param left: The leftmost coordinate of where to draw the Button
		:param top: The top coordinate of where to draw the Button
		:param width: The width of the Button
		:param height: The height of the Button
		:param text: The text to display inside of the Button
		:param action: The action to me invoked when clicking on the Button
		:return: returns an instance of the Button object
		"""
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