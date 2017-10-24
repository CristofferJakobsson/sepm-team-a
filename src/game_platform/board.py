import math

def adjustMousePos(mousepos, offset):
    """
    Adjusts the given mouse position coordinates according to the given offset.

    :param mousepos: The coordinates of the given mouse position
    :param offset: Offsets to apply to the mouse position coordinates
    :return: returns the given mouse position adjusted by the given offset
    """
    return ((mousepos[0]-offset[0]), mousepos[1]-offset[1])

class Board:
    """
	Board is the graphical interface for the Game Platform which displays the Tic Tac Toe game and draws different moves on the screen
	"""
    def __init__(self, ui, player1, player2):
        """
		Construct a new Board object.

		:param self: A reference to the Board object itself
		:param ui: A reference to the GameUI object
		:return: returns nothing
		"""
        self.player1 = player1
        self.player2 = player2
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

    def drawCross(self, box, iconWidth=-1):
        """
		Draws a cross on the screen within a given box of the Tic Tac Toe game.

		:param self: A reference to the Board object itself
		:param box: An object containing the coordinates of the box which is to contain the cross that is to be drawn.
		:param iconWidth: The width to use for the drawn cross.
		:return: returns nothing
		"""
        if iconWidth == -1:
            iconWidth = self.iconthickness
        start1 = ((box.left + self.iconoffset), (box.top + self.iconoffset))
        end1 = ((box.right-self.iconoffset), (box.bottom-self.iconoffset))

        start2 = ((box.right - self.iconoffset), (box.top + self.iconoffset))
        end2 = ((box.left + self.iconoffset), (box.bottom - self.iconoffset))

        self.pygame.draw.line(self.gameArea, self.color_cross, start1, end1, iconWidth)
        self.pygame.draw.line(self.gameArea, self.color_cross, start2, end2, iconWidth)

    def drawCircle(self, box, iconWidth=-1):
        """
		Draws a circle on the screen within a given box of the Tic Tac Toe game.

		:param self: A reference to the Board object itself
		:param box: An object containing the coordinates of the box which is to contain the circle that is to be drawn.
        :param iconWidth: The width to use for the drawn circle.
		:return: returns nothing
		"""
        #circle(Surface, color, pos, radius, width=0) -> Rect
        if iconWidth == -1:
            iconWidth = self.iconthickness
        self.pygame.draw.circle(self.gameArea,
                                self.color_circle,
                                box.center,
                                math.floor((box.height - self.iconoffset)/2),
                                iconWidth)

    def updateBoardState(self, state):
        """
		Updates the current Board's state and draws crosses and circles depending on the different values of the boxes within the board.

		:param self: A reference to the Board object itself
		:param state: The updated Board state, a list with each index representing a box in the Tic Tac Toe grid. A -1 represents a circle, 1 represents a cross and 0 an open box
		:return: returns nothing
		"""
        self.ui.renderTop(self.player1, self.player2, self.ui.game.currentplayer)
        for box in self.boxes:
            if state[box.id] == 1:
                self.drawCross(box.rect)
            if state[box.id] == -1:
                self.drawCircle(box.rect)

    def drawBoard(self):
        """
		Invokes the initBoard function to draw the Board on the screen.

		:param self: A reference to the Board object itself
		:return: returns nothing
		"""
        self.initBoard()

    def initBoard(self):
        """
		Draws the Board object on the screen.

		:param self: A reference to the Board object itself
		:return: returns nothing
		"""
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
        """
		Find the box in the Tic Tac Toe grid that was clicked on by the user.

		:param self: A reference to the Board object itself
		:param mousepos: The position of where the mouse was when clicked
		:return: The index of the box that was clicked, if no box was clicked: returns -1
		"""
        for box in self.boxes:
            if box.checkMouseClick(adjustMousePos(mousepos, self.gameArea.get_abs_offset())):
                return box.id
        return -1

    def drawWinBoard(self, player):
        """
		Draws the win board on the screen.

		:param self: A reference to the Board object itself
		:param player: A reference to the winning player
		:return: returns nothing
		"""
        self.gameArea.fill(self.ui.color_background)
        iconRect = self.pygame.Rect(35, 0, self.gameArea.get_width()-35, self.gameArea.get_height()-70)
        if(player == 1):
            self.drawCross(iconRect, 35)
        if(player == -1):
            self.drawCircle(iconRect, 35)

        coords = 110, 330
        color = (0,0,0)
        font = self.pygame.font.SysFont("sans", 52)
        txt = font.render("WINNER", True, color)
        self.gameArea.blit(txt, coords)
        self.pygame.display.flip()

    def drawDrawBoard(self):
        """
		Draws the draw board on the screen.

		:param self: A reference to the Board object itself
		:return: returns nothing
		"""
        self.gameArea.fill(self.ui.color_background)

        coords1 = 110, 170
        coords2 = 110, 220
        coords3 = 110, 270
        coords4 = 110, 320
        color = (0,0,0)
        font = self.pygame.font.SysFont("sans", 52)
        row1 = font.render("It's", True, color)
        row2 = font.render("A", True, color)
        row3 = font.render("Goddamn", True, color)
        row4 = font.render("Draw!!", True, color)
        self.gameArea.blit(row1, coords1)
        self.gameArea.blit(row2, coords2)
        self.gameArea.blit(row3, coords3)
        self.gameArea.blit(row4, coords4)

    def displayTournamentDrawInfo(self, countdown):
        """
		Displays information about a draw game in the tournament.

		:param self: A reference to the Board object itself
		:param countdown: number of games that were decided by draw
		:return: returns nothing
		"""
        self.gameArea.fill(self.ui.color_background)

        coords1 = 110, 170
        coords2 = 110, 220
        coords3 = 110, 270
        coords4 = 110, 320
        color = (0,0,0)
        font = self.pygame.font.SysFont("sans", 52)

        row1_string = "DRAW!"
        row2_string = "Randomize"
        row3_string = "winner in"
        row4_string = str(countdown) + " game"
        if(countdown != 1):
            row4_string += "s"

        row1 = font.render(row1_string, True, color)
        row2 = font.render(row2_string, True, color)
        row3 = font.render(row3_string, True, color)
        row4 = font.render(row4_string, True, color)
        self.gameArea.blit(row1, coords1)
        self.gameArea.blit(row2, coords2)
        self.gameArea.blit(row3, coords3)
        self.gameArea.blit(row4, coords4)

        self.ui.pygame.display.flip()

    def displayRandomizingWinner(self):
        """
		Displays text for randomizing winner.

		:param self: A reference to the Board object itself
		:return: returns nothing
		"""
        self.gameArea.fill(self.ui.color_background)

        coords1 = 110, 170
        coords2 = 110, 220

        color = (0,0,0)
        font = self.pygame.font.SysFont("sans", 52)

        row1_string = "Randomizing"
        row2_string = "winner..."


        row1 = font.render(row1_string, True, color)
        row2 = font.render(row2_string, True, color)

        self.gameArea.blit(row1, coords1)
        self.gameArea.blit(row2, coords2)

        self.ui.pygame.display.flip()


    class Box:
        """
	    Box represents a rectangle within the Tic Tac Toe grid
	    """
        def __init__(self, rect, id):
            """
            Construct a new Box object.

            :param self: A reference to the Box object itself
            :param rect: The rectangle which the Box represents
            :param id: A unique id for the Box
            :return: returns nothing
            """
            self.rect = rect
            self.id = id

        def checkMouseClick(self, mousepos):
            """
            Checks if a given mouse click was within the Box's coordinates

            :param self: A reference to the Box object itself
            :param mousepos: The position of where the mouse was when clicked
            :return: returns a boolean condition whether the mouse click's coordinates was within the Box coordinates
            """
            return self.rect.collidepoint(mousepos)
