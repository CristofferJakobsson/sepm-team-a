class TournamentGame:

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.winner = None

	def setWinner(self, player):
		self.winner = player
