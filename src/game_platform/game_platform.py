from board import Board
import random
from player import Player, Human, Computer
class Game:
    """
	Game is the main class for the Game Platform Interface
	"""
    def __init__(self, ui, player1, player2):
        """
		Construct a new Game object.

		:param self: A reference to the Game object itself
		:param ui: The user interface for the Game object
		:param player1: A reference to Player 1 in the current Game
		:param player2: A reference to Player 2 in the current Game
		:return: returns nothing
		"""
        self.player1 = player1
        self.player2 = player2

        self.gameState =   [0, 0, 0,
                            0, 0, 0,
                            0, 0, 0]

        self.ui = ui
        self.currentplayer = 1
        if random.uniform(0, 1) > 0.5:
            self.currentplayer = -1

        self.displayBoard(ui)

    def displayBoard(self, ui):
        """
		Displays the Game's user interface

		:param self: A reference to the Game object itself
		:param ui: The user interface to display
		:return: returns nothing
		"""
        self.board = Board(ui)

    def checkWin(self):
        """
		Checks if a Player in the Game reached winning conditions

		:param self: A reference to the Game object itself
		:return: returns nothing
		"""
        winstates = [(0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 8),
                     (2, 4, 6)]
        for state in winstates:
            if (self.gameState[state[0]] + self.gameState[state[1]] + self.gameState[state[2]]) == 3:
                return 1
            if (self.gameState[state[0]] + self.gameState[state[1]] + self.gameState[state[2]]) == -3:
                return -1
        if len([i for i in range(9) if self.gameState[i] == 0]) == 0:
            return 0
        return None

    def validmove(self, boxId):
        """
		Checks if a given move is valid

		:param self: A reference to the Game object itself
		:param boxId: the given index to be checked if a move can be made upon
		:return: returns a boolean deciding whether the given move is valid
		"""
        return ((self.gameState[boxId] == 0) and (0 <= boxId <= 8))

    def gameTic(self):
        """
		Performs a Player move if it's valid

		:param self: A reference to the Game object itself
		:return: returns nothing
		"""
        boxId = -1

        if self.currentplayer == 1:
            boxId = self.player1.play(self.gameState)
        if self.currentplayer == -1:
            boxId = self.player2.play(self.gameState)

        if self.validmove(boxId):
            self.makemove(boxId)


    def makemove(self,boxId):
        """
		Performs a move for the current player.

		:param self: A reference to the Game object itself
		:param boxId: The index of where the move will be done in the game state list
		:return: returns nothing
		"""
        self.gameState[boxId] = self.currentplayer
        self.currentplayer = self.currentplayer * -1
        self.board.updateBoardState(self.gameState)

    def click(self, mousepos):
        """
		Handles mouse clicks within the Game coordinates

		:param self: A reference to the GameUI object itself
		:param mousepos: The coordinates of where the mouse was clicked
		:return: returns a boolean whether current Player has won
		"""
        if self.currentplayer == 1:
            if isinstance(self.player1, Computer):
                return
            else:
                self.player1.move = self.board.findClickedBox(mousepos)
        if self.currentplayer == -1:
            if isinstance(self.player2, Computer):
                return
            else:
                self.player2.move = self.board.findClickedBox(mousepos)