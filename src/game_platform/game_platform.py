from board import Board
import random

class Game:
    def __init__(self, ui, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.gameState =   [0, 0, 0, 
                            0, 0, 0, 
                            0, 0, 0]

        self.ui = ui
        # self.nextplayer = 1
        self.currentplayer = 1
        if random.uniform(0, 1) > 0.5:
            self.currentplayer = -1

        self.displayBoard(ui)

    def displayBoard(self, ui):
        self.board = Board(ui)

    def checkWin(self):
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
                return 2
        return 0


    def makemove(self,boxId):
        self.gameState[boxId] = self.currentplayer

        self.board.updateBoardState(self.gameState)
        
        self.currentplayer = self.currentplayer * -1

    def click(self, mousepos):
        boxId = self.board.findClickedBox(mousepos)
        if self.gameState[boxId] != 0:
            return
        
        self.makemove(boxId)


        return self.checkWin()