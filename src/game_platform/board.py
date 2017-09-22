import pygame

class Board:
    
    def __init(self, player1, player2, gameArea, pygame)__:
        self.gameState =   (0, 0, 0, 
                        0, 0, 0, 
                        0, 0, 0)
        self.player1 = player1
        self.player2 = player2
        self.gameArea = gameArea
        self.pygame = pygame


        self.drawBoard(self, gameState, gameArea)

    def drawBoard(self):
        self.drawGrid(self.gameArea)


    def drawGrid(self):
        height = self.gameArea.get_height()
        width = self.gameArea.get_width()

        start1 = (height/3, 0)
        end1 = (height/3, width)
        
        self.pygame.draw.line(self.gameArea, Color(120, 120, 120, 0.3), start1, end1, 10)