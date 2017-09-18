import datetime, random, pygame, sys, time
from button import Button


class GameUI: 
    def __init__(self): 
        self.WINDOW_SIZE = width, height = 1280, 720
        self.TOP_RATIO = 2/7
        self.BOTTOM_RATIO = 5/7

        self.color_background = pygame.Color(83, 178, 162)
        self.color_menu = pygame.Color(247, 247, 247)
        self.color_border = pygame.Color(144, 148, 150)
        self.color_lighttext = pygame.Color(149, 152, 154)
        self.color_darktext = pygame.Color(74, 74, 74)

        pygame.init()

        pygame.display.set_caption("Tic Tac Toe")

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.mainArea = self.screen.subsurface(
            self.screen.fill(
                self.color_background, 
                pygame.Rect(
                    0, 
                    self.screen.get_height()*self.TOP_RATIO, 
                    self.screen.get_width(), 
                    self.screen.get_height()*self.BOTTOM_RATIO
                )
            )
        )
        
        self.secondaryArea = self.screen.subsurface(
            self.screen.fill(
                self.color_menu, 
                pygame.Rect(
                    0, 
                    0, 
                    self.screen.get_width(), 
                    self.screen.get_height()*self.TOP_RATIO
                )
            )
        )
        
        self.border   = pygame.draw.line(
            self.screen, 
            self.color_border, 
            (0, self.screen.get_height()*self.TOP_RATIO), 
            (self.screen.get_width(), 
            self.screen.get_height()*self.TOP_RATIO), 
            2
        )
        
        self.buttonMaker = Button(pygame, self.mainArea)


        self.displayMainMenu()
    
    def checkButtonClick(self, pos):
        for button in self.visiblebuttons: 
            print("button")

    def tic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: self.checkButtonClick(pygame.mouse.get_pos())
        pygame.display.flip()

    def displayMainMenu(self):
        buttonHalfWidth = 200
        buttonHeight = 50

        self.visiblebuttons = (
            self.buttonMaker.create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                50, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player vs Computer", 
                True
            ), 
            self.buttonMaker.create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                110, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player vs Player", 
                True
            ),         
            self.buttonMaker.create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                170, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player Tournament", 
                True
            ), 
            self.buttonMaker.create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                400, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Exit", 
                True
            )      
        )
        




ui = GameUI()
while 1:
    ui.tic()
