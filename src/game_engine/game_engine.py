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
			return rm
		else:
			return mm

	def hardmove(self, board, currentplayer):
		"""
		The Best move for the given Player (Computer) to make among possible moves.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:return: returns the move for the Player to make
		"""

		player, move = self.minmax(board, currentplayer, currentplayer)
		return move


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

	def minmax(self, board, currentplayer, max_player):
		"""
		Minimax decision rule to decide the move for the given Player by minimizing the loss for the worst case scenario move.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:param max_player: The player we want to win.
		:return: the Player and the best move for that Player
		"""
		return self.nextMove(board, currentplayer, max_player)

	def nextMove(self, board, currentplayer, max_player):
		"""
		Next move decided by minimax decision rule to decide the move for the given Player by minimizing the loss for the worst case scenario move.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param currentplayer: A reference to the Computer object whose move is to be decided
		:param max_player: The player we want to win.
		:return: the Player and the best move for that Player
		"""
		if self.game_over(board):
			if self.winning(board, max_player): return 1,1
			elif self.winning(board, max_player*-1): return -1,-1
			else: return 0,0
		else:
			avail = self.available_moves(board)
			c = len(avail)
			if  c == 9: return 1,4

			nextplayer = currentplayer * -1
			newboard = []

			for i in avail:
				board[i] = currentplayer
				ret,move = self.nextMove(board, nextplayer, max_player)
				newboard.append(ret)
				board[i] = 0

			if currentplayer == max_player:
				maxele = max(newboard)
				return maxele,avail[newboard.index(maxele)]
			else:
				minele = min(newboard)
				return minele,avail[newboard.index(minele)]


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

	def game_over(self,board):
		"""
		Checks if the game is over.

		:param self: A reference to the game_engine object itself
		:param board: A reference to the current game board
		:param player: A reference to the current game board
		:return: returns a boolean whether the game is over or not
		"""
		if len(self.available_moves(board)) == 0:
			return True
		elif self.winning(board, 1):
			return True
		elif self.winning(board, -1):
			return True
		else:
			return False