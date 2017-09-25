import random

class Tournament:
	"""
	Tournament encapsulates a number of players and handles the tournament mode of the game.
	"""
	def __init__(self, players):
		"""
		Construct a new Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		self.players = []
		self.ontothenext = []
		self.matches = []

		# Check names are not blank
		for n in range(len(players)):
			if len(players[n]) > 0:
				self.players.append(players[n])
		# random.shuffle(self.players)

		# check we have an even numer of players
		if len(self.players) % 2 != 0:
			print("uneaven number of players given...")
			# move one player to next round.
			# r = random.randint(0, len(self.players)-1)
			r = 1
			self.ontothenext.append(self.players[r])
			self.players.remove(self.players[r])
			print("player to move to next round: " + str(r))

		self.makeMatches()

	def debug(self):
		"""
		Prints out variables belonging to the Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		print(self.players)
		print(self.matches)
		print(self.ontothenext)

	def getMatches(self):
		"""
		Returns the number of matches belonging to the Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		return self.matches
	def makeMatches(self):
		"""
		Appends a match to the Tournament object for each player belonging to the Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		for n in range(len(self.players) / 2):
			self.matches.append([
				self.players[n],
				self.players[len(self.players)-n-1]
				])

	def setWinner(self, playername):
		"""
		Appends the current winners to a list belonging to the Tournament object which contains the players advancing to the next round.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		self.ontothenext.append(playername)
		if len(self.matches) == 1:
			self.matches = []
		for n in range(len(self.matches)-1):
			if self.matches[n][0] == playername:
				del self.matches[n]
			if self.matches[n][1] == playername:
				del self.matches[n]



def main():
	t = Tournament(["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "", "Player 7", "Player 8"])
	t.debug()
	t.setWinner("Player 1")
	t.debug()
	t.setWinner("Player 3")
	t.debug()
	t.setWinner("Player 5")
	t.debug()
if __name__ == '__main__': main()