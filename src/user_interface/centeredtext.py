class centeredtext(object):
  """
  centeredtext encapsulates a centered text within a given object
  """
  def __init__(self, text, x,y,w,h, pygame, fontsize, color=(0,0,0)):
    """
    Construct a new 'centeredtext' object.

    :param text: The text to center within the given object
    :param x: The leftmost coordinate of the given object of which to center a text within
    :param y: The rightmost coordinate of the given object of which to center a text within
    :param w: The width of the given object of which to center a text within
    :param h: The height of the given object of which to center a text within
    :param pygame: The pygame instance running
    :param fontsize: The fontsize of the text to center
    :param color: The color of the text to center
    :return: returns nothing
    """
    self.pygame = pygame
    self.x, self.y, self.w, self.h = x,y,w,h
    self.pygame.font.init()
    font = self.pygame.font.SysFont("sans", fontsize)
    width, height = font.size(text)
    xoffset = (self.w-width) // 2
    yoffset = (self.h-height) // 2
    self.coords = self.x+xoffset, self.y+yoffset
    self.txt = font.render(text, True, color)

  def draw(self, screen, bordercolor):
    """
    Display the centered text object within the given object.

    :param self: A reference to the centeredtext object itself
    :param screen: The screen where to display the text
    :param bordercolor: The border color of the testing rect
    :return: returns nothing
    """
    screen.blit(self.txt, self.coords)
    # for testing purposes, draw the rectangle too
    rect = self.pygame.Rect(self.x, self.y, self.w, self.h)
    self.pygame.draw.rect(screen, bordercolor, rect, 1)