

class Board:
    
    def __init__(self, ui):
        self.gameState =   (0, 0, 0, 
                        0, 0, 0, 
                        0, 0, 0)
        self.player1 = ui.playernames[0]
        self.player2 = ui.playernames[1]
        self.ui = ui
        self.pygame = ui.pygame
        self.gameArea = ui.mainArea.subsurface(
                self.pygame.Rect(
                    ui.mainArea.get_width()/2-200, 
                    ui.mainArea.get_height()/2-200, 
                    400, 
                    400
            ))
        self.drawBoard()

    def drawBoard(self):
        self.drawGrid()


    def drawGrid(self):
        height = self.gameArea.get_height()
        width = self.gameArea.get_width()

        start1 = (height/3, 0)
        end1 = (height/3, width)
        
        self.pygame.draw.line(self.gameArea, self.pygame.Color(120, 120, 120), start1, end1, 10)