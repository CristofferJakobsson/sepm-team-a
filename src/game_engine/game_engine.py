import random
from sys import stdout

class game_engine:
	"""
	game_engine is the class that controls Computer moves, keeps track of game state such as possible moves and if a player has won
	"""
	def __init__(self, level):
		"""
		Construct a new game_engine object.

		:param self: A reference to the game_engine object itself
		:return: returns nothing
		"""
		self.level = level

	def makemove(self, board, currentplayer):
		"""
		Decides on what kind of move the given Player (Computer) should make depending on its difficulty level.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:return: returns the move for the Player to make
		"""

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
		"""
		The Best move for the given Player (Computer) to make among possible moves.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:return: returns the move for the Player to make
		"""
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
		"""
		A random move, among possible moves for the Player (Computer) to make.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:return: returns the move for the Player to make
		"""
		temp = self.available_moves(board)
		random.shuffle(temp)
		return temp[0]

	def minmax(self, board, currentplayer, alpha, beta):
		"""
		Minimax decision rule to decide the move for the given Player by minimizing the loss for the worst case scenario move.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:param alpha: TODO
		:param beta: TODO
		:return: TODO
		"""
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
		"""
		A list containing current possible moves.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:return: returns a list containing current possible moves
		"""
		return [i for i in range(9) if board[i] == 0]

	def winning(self, board, player):
		"""
		Checks if given Player has won.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param player: A reference to the current game board
		:return: returns a boolean whether the given Player has won
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
			if board[state[0]] == player and board[state[1]] == player and board[state[2]] == player:
				return True

		return False