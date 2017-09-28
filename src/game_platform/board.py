import math

def adjustMousePos(mousepos, offset):
    return ((mousepos[0]-offset[0]), mousepos[1]-offset[1])

class Board:

    def __init__(self, ui):
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
        self.boxes = []

        self.iconoffset = 15
        self.color_cross = self.pygame.Color(75, 75, 75)
        self.color_circle = self.pygame.Color(240, 235, 202)
        self.iconthickness = 15

        self.drawBoard()

    def drawCross(self, box):

        start1 = ((box.left + self.iconoffset), (box.top + self.iconoffset))
        end1 = ((box.right-self.iconoffset), (box.bottom-self.iconoffset))

        start2 = ((box.right - self.iconoffset), (box.top + self.iconoffset))
        end2 = ((box.left + self.iconoffset), (box.bottom - self.iconoffset))

        self.pygame.draw.line(self.gameArea, self.color_cross, start1, end1, self.iconthickness)
        self.pygame.draw.line(self.gameArea, self.color_cross, start2, end2, self.iconthickness)

    def drawCircle(self, box):
        #circle(Surface, color, pos, radius, width=0) -> Rect
        self.pygame.draw.circle(self.gameArea, self.color_circle, box.center, math.floor((box.height - self.iconoffset)/2), self.iconthickness)

    def updateBoardState(self, state):
        self.ui.renderTop(self.player1, self.player2, self.ui.game.currentplayer)
        for box in self.boxes:
            if state[box.id] == 1:
                self.drawCross(box.rect)
            if state[box.id] == -1:
                self.drawCircle(box.rect)

    def drawBoard(self):
        self.initBoard()

    def initBoard(self):
        height = self.gameArea.get_height()
        width = self.gameArea.get_width()

        borderSize = 10
        boxWidth = width/3 - borderSize
        boxHeight = height/3 - borderSize


        boxId = 0
        for y in range(0,3):
            for x in range(0, 3):
                box = self.Box(
                    self.ui.pygame.Rect(
                        (boxWidth+borderSize)*x,
                        (boxHeight+borderSize)*y,
                        boxWidth+(borderSize/2),
                        boxHeight+(borderSize/2)),
                    boxId)
                self.boxes.append(box)
                boxId += 1


#        for box in self.boxes:
#            self.drawCircle(box.rect)
#            self.gameArea.fill(self.ui.pygame.Color(0, 0, 0), box)

        start1 = (0, height/3)
        end1 = (width, height/3)
        self.pygame.draw.line(self.gameArea, self.ui.color_darkgreen, start1, end1, 10)

        start2 = (0, height*(2/3))
        end2 = (width, height*(2/3))
        self.pygame.draw.line(self.gameArea, self.ui.color_darkgreen, start2, end2, 10)

        start3 = (height/3, 0)
        end3 = (height/3, width)
        self.pygame.draw.line(self.gameArea, self.ui.color_darkgreen, start3, end3, 10)

        start4 = (height*(2/3), 0)
        end4 = ( height*(2/3), width)
        self.pygame.draw.line(self.gameArea, self.ui.color_darkgreen, start4, end4, 10)

    def findClickedBox(self, mousepos):
        for box in self.boxes:
            if box.checkMouseClick(adjustMousePos(mousepos, self.gameArea.get_abs_offset())):
                return box.id
        return -1


    class Box:
        def __init__(self, rect, id):
            self.rect = rect
            self.id = id

        def checkMouseClick(self, mousepos):
            return self.rect.collidepoint(mousepos)
