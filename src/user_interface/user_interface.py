import datetime, random, pygame, sys, time

class GameUI: 
    
    def __init__(self): 
        self.WINDOW_SIZE = width, height = 1280, 720
        self.TOP_RATIO = 2/7
        self.BOTTOM_RATIO = 5/7

        self.gameColor = pygame.Color(83, 178, 162)
        self.menuColor = pygame.Color(247, 247, 247)
        self.borderColor = pygame.Color(144, 148, 150)

        pygame.init()   

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.mainArea = self.screen.subsurface(self.screen.fill(self.gameColor, pygame.Rect(0, self.screen.get_height()*self.TOP_RATIO, self.screen.get_width(), self.screen.get_height()*self.BOTTOM_RATIO)))
        self.secondaryArea = self.screen.subsurface(self.screen.fill(self.menuColor, pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height()*self.TOP_RATIO)))
        self.border   = pygame.draw.line(self.screen, self.borderColor, (0, self.screen.get_height()*self.TOP_RATIO), (self.screen.get_width(), self.screen.get_height()*self.TOP_RATIO), 3)
        self.displayMainMenu()

    def tic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()

    def displayMainMenu(self):
        buttonHalfWidth = 200
        buttonHeight = 50


        Button(self, self.WINDOW_SIZE[0]/2-buttonHalfWidth, buttonHeight, buttonHalfWidth*2, buttonHeight, "Player VS Computer", True)      
        

class Button:
    def __init__(self, ui, left, top, width, height, text, action):
        
        buttonTextFont = pygame.font.Font('freesansbold.ttf', 28)
        pvcButtonRect = ui.mainArea.blit(buttonTextFont.render(text, True, (0,0,0)), ui.mainArea.fill(ui.menuColor, pygame.Rect(left, top, width, height)))


ui = GameUI()
while 1:
    ui.tic()
