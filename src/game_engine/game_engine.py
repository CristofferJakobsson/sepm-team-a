import random
from sys import stdout

class game_engine:

	def __init__(self, level):
		self.level = level

	def makemove(self,board,currentplayer): 
		rm = self.randommove(board, currentplayer)
		mm = self.hardmove(board, currentplayer) 

		if self.level == "hard":
			q = 1
		elif self.level == "normal":
			q = 0.75
		else:
			q = 0.30

		if random.uniform(0, 1) > q:
			print("Making random move")
			return rm
		else:
			print("Making hard move")
			return mm

	def hardmove(self, board, currentplayer):
		avail = self.available_moves(board)
		nextplayer = currentplayer * -1
		choises = []
		a = -2
		if len(avail) == 9: 
			return 4

		for i in avail:
			newboard = board[:]
			newboard[i] = currentplayer
			val = self.minmax(newboard, nextplayer, -2, 2)
			if val > a: 
				a = val
				choises = [i]
			elif val == a:
				choises.append(i)
		random.shuffle(choises)
		return choises.pop()


	def randommove(self,board,currentplayer):
		temp = self.available_moves(board)
		random.shuffle(temp)
		return temp[0]

	def minmax(self, board,currentplayer, alpha, beta):
		possible_moves = self.available_moves(board)
		nextplayer = currentplayer * -1
		
		if len(possible_moves) == 0:
			return 0
		elif self.winning(board, currentplayer):
			return currentplayer
		elif self.winning(board, nextplayer):
			return nextplayer
		
		for i in possible_moves:
			newboard = board[:]
			newboard[i] = currentplayer
			val = self.minmax(newboard, nextplayer, alpha, beta)
			if currentplayer == 1:
				if val > alpha:
					alpha = val
				if alpha >= beta:
					return beta
			else:
				if val < beta:
					beta = val
				if beta <= alpha:
					return alpha

		if currentplayer == 1:
			return alpha
		else:
			return beta

	def available_moves(self,board):
		return [i for i in range(9) if board[i] == 0]

	def winning(self, board, player):
		winstates = [(0, 1, 2),
					 (3, 4, 5),
					 (6, 7, 8),
					 (0, 3, 6),
					 (1, 4, 7),
					 (2, 5, 8),
					 (0, 4, 8),
					 (2, 4, 6)]
		for state in winstates:
			if board[state[0]] == player and board[state[1]] == player and board[state[2]] == player:
				return True
			
		return False



