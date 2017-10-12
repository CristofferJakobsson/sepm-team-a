class TournamentGame:
	"""
	TournamentGame encapsulates two players, keeps count of the winner and the number of games played
	"""
	def __init__(self, player1, player2):
		"""
		Construct a new TournamentGame object.

		:param self: A reference to the TournamentGame object itself
		:param player1: The first of the players in the tournament game
		:param player1: The second of the players in the tournament game
		:return: returns nothing
		"""
		self.player1 = player1
		self.player2 = player2
		self.winner = None
		self.gamecount = 0

	def setWinner(self, player):
		"""
		Sets a winner for the tournament game.

		:param self: A reference to the TournamentGame object itself
		:param player: the player to be set as a winner
		:return: returns nothing
		"""
		self.winner = player
