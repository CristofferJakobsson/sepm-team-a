import random
from tournament_game import TournamentGame
from button import Button

class Tournament:
	"""
	Tournament encapsulates a number of players and handles the tournament mode of the game.
	"""
	def __init__(self, ui, players):
		"""
		Construct a new Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		self.currentGame = 0
		self.ui = ui
		self.players = []
		self.ontothenext = []
		self.matches = []

		if len(players) >= 4:
			self.maxrows = 4
		else:
			self.maxrows = 2

		# Check names are not blank
		for n in range(len(players)):
			if len(players[n]) > 0:
				self.players.append(players[n])
		random.shuffle(self.players)


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

	def getNextMatch(self): 
		# if more then two players create a new match.
		if len(self.players) >= 2:
			self.makeMatches()
		
		mem = self.currentGame
		
		if self.matches[mem]:
			self.currentGame = self.currentGame + 1
			return 2,self.matches[mem]
		else:
			return 1,self.players 


	def drawBracket(self):
		xoffset = 240
		yoffset = 50

		xstart = 300
		ystart = 10

		x = xstart
		y = ystart
		rows = 0
		cols = 1
		for match in self.matches:
			self.drawMatch(match, x, y)
			rows = rows + 1
			if rows == self.maxrows:
				self.maxrows = self.maxrows -1
				cols = cols + 1
				rows = 1
				x = x + xoffset
				if cols == 3:
					yoffset = (yoffset * cols)
				else:
					yoffset = (yoffset * cols)/2
				y = ystart + yoffset
			else:
				if cols == 2:
					y = y + yoffset*4
				elif cols == 1:
					y = y + yoffset*2
				else:	
					y = y + yoffset*2
				


	def drawMatch(self, match, x, y):
		print(match.player1 +" "  + match.player2 + " " + str(x) + " " + str(y))
		width = 200
		height = 40
		self.ui.visiblebuttons.append(
			Button(self.ui.pygame, self.ui.mainArea).create(
				self.ui.color_menu,
				self.ui.color_darktext,
				self.ui.color_border,
				x,
				y,
				width,
				height,
				match.player1,
				self.drawBracket
			)
		)

		self.ui.visiblebuttons.append(
			Button(self.ui.pygame, self.ui.mainArea).create(
				self.ui.color_menu,
				self.ui.color_darktext,
				self.ui.color_border,
				x,
				y+height+5,
				width,
				height,
				match.player2,
				self.drawBracket
			)
		)


	def makeMatches(self):
		"""
		Appends a match to the Tournament object for each player belonging to the Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""
		for n in range(int(len(self.players) / 2)):
			self.matches.append(TournamentGame(self.players[n], self.players[len(self.players)-n-1]))

	# def setWinner(self, playername):
	# 	"""
	# 	Appends the current winners to a list belonging to the Tournament object which contains the players advancing to the next round.

	# 	:param self: A reference to the Tournament object itself
	# 	:return: returns nothing
	# 	"""
	# 	self.ontothenext.append(playername)
	# 	if len(self.matches) == 1:
	# 		self.matches = []
	# 	for n in range(len(self.matches)-1):
	# 		if self.matches[n][0] == playername:
	# 			del self.matches[n]
	# 		if self.matches[n][1] == playername:
	# 			del self.matches[n]
