class centeredtext(object):

    def __init__(self, text, x,y,w,h, pygame,color=(0,0,0)):
        self.pygame = pygame
        self.x, self.y, self.w, self.h = x,y,w,h
        self.pygame.font.init()
        font = self.pygame.font.SysFont("sans", 20)
        width, height = font.size(text)
        xoffset = (self.w-width) // 2
        yoffset = (self.h-height) // 2
        self.coords = self.x+xoffset, self.y+yoffset
        self.txt = font.render(text, True, color)

    def draw(self, screen):
        screen.blit(self.txt, self.coords)
        # for testing purposes, draw the rectangle too
        rect = Rect(self.x, self.y, self.w, self.h)
        self.pygame.draw.rect(screen, (0,0,0), rect, 1)