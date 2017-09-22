import datetime, random, pygame, sys, time
from button import Button
from centeredtext import centeredtext
from board import Board

def actionPrint():
    print("test")   

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
        

        title = centeredtext("Tic Tac Toe", 0,0, 1280, 75, pygame, 100, self.color_lighttext)
        title.draw(self.secondaryArea, self.color_menu)

        self.border   = pygame.draw.line(
            self.screen, 
            self.color_border, 
            (0, self.screen.get_height()*self.TOP_RATIO), 
            (self.screen.get_width(), 
            self.screen.get_height()*self.TOP_RATIO), 
            2
        )
        
        self.displayMainMenu()
    
    def checkButtonClick(self, pos):
        for button in self.visiblebuttons: 
            offset = button.area.get_offset()
            if (button.box.collidepoint((pos[0]-offset[0]), (pos[1]-offset[1]))): button.action()

    def tic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: self.checkButtonClick(pygame.mouse.get_pos())
            
        pygame.display.flip()

    def displayMainMenu(self):
        self.mainArea.fill(self.color_background)
        buttonHalfWidth = 200
        buttonHeight = 50

        self.visiblebuttons = (
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                50, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player vs Computer", 
                self.displayGame
            )), 
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                110, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player vs Player", 
                self.displayGame
            )),         
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                170, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Player Tournament", 
                self.displayCreateTournament
            )), 
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                self.WINDOW_SIZE[0]/2-buttonHalfWidth, 
                400, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Exit", 
                sys.exit
            ))      
        )

    def displayGame(self):
        self.mainArea.fill(self.color_background)
        buttonHalfWidth = 150
        buttonHeight = 50

        self.visiblebuttons = (
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                100, 
                450, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Back", 
                self.displayMainMenu
            )),
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                900, 
                450, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Forfit", 
                self.displayMainMenu
            ))
        )

    def displayCreateTournament(self):
        self.mainArea.fill(self.color_background)
        buttonHalfWidth = 150
        buttonHeight = 50
        
        self.visiblebuttons = (
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                100, 
                450, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Back", 
                self.displayMainMenu
            )),
            (Button(pygame, self.mainArea).create(
                self.color_menu,
                self.color_darktext,
                self.color_border,
                900, 
                450, 
                buttonHalfWidth*2, 
                buttonHeight, 
                "Start Tournament", 
                self.displayMainMenu
            ))
        )

        def spawnGame(self):
            game = Board("P1", "P2", )


ui = GameUI()
while 1:
    ui.tic()
