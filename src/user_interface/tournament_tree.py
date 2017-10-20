import random
from tournament_game import TournamentGame
from button import Button
import sys

sys.path.insert(0, '../game_platform')
from player import Player, Human, Computer


class Tournament:
	"""
	Tournament encapsulates a number of players and handles the tournament mode of the game.
	"""
	def __init__(self, ui, players):
		"""
		Construct a new Tournament object.

		:param self: A reference to the Tournament object itself
		:param ui: A reference to the GameUI object
		:param players: a list containing names of players in the tournament
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
				self.players.append(Human(players[n]))



		c = 1
		while 1:
			if len(self.players) % 4 == 0:
				break

			level = 0

			while(level not in [1,2,3]):
				try:
					level = int(self.ui.askfornames.ask("AI level: (1, 2, 3)"))
				except ValueError:
					pass

			if level == 1:
				l = "easy"
			elif level == 2:
				l = "normal"
			else:
				l = "hard"
			self.players.append(Computer("Computer " + str(c), l))
			c = c + 1

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
		:return: returns the matches belonging to the Tournament object
		"""
		return self.matches

	def getNextMatch(self):
		"""
		Fetches the next match to be played in the tournament.

		:param self: A reference to the Tournament object itself
		:return: returns the players to play in the next match and the number of times those players have met in a row, including the next match
		"""
		mem = self.currentGame

		if mem < len(self.currentGame) -1:
			self.currentGame = self.currentGame + 1
			return 2,self.matches[mem]
		else:
			return 1,self.players


	def getCurrentMatch(self):
		"""
		Fetches the current match.

		:param self: A reference to the Tournament object itself
		:return: returns the players to play in the current match and the number of times those players have met in a row, including the current match
		"""
		mem = self.currentGame-1
		if mem < len(self.currentGame) -1:
			return 2,self.matches[mem]
		else:
			return 1, self.players


	def drawBracket(self):
		"""
		Draws the bracket of the tournament.

		:param self: A reference to the Tournament object itself
		:return: retuerns nothing
		"""
		if len(self.players) >= 2:
			self.makeMatches()

		xoffset = 240
		yoffset = 50

		xstart = 300
		ystart = 10

		x = xstart
		y = ystart
		rows = 0
		cols = 1
		nextpicked = None
		maxrows = self.maxrows
		for match in self.matches:
			if nextpicked == None and match.winner == None:
				self.drawMatch(match, x, y, True)
				nextpicked = True
			else:
				self.drawMatch(match, x, y)
			rows = rows + 1
			if rows == maxrows:
				maxrows = maxrows - 1
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



	def drawMatch(self, match, x, y, is_next = False):
		"""
		Draws a match in the tournament bracket.

		:param self: A reference to the Tournament object itself
		:param match: A reference to the match to be drawn
		:param x: Horizontal coordinate for where to begin to draw the next match
		:param y: Vertical coordinate for where to begin to draw the next match
		:param is_next: A boolean deciding whether the given match is the next to be played
		:return: retuerns nothing
		"""
		width = 200
		height = 40

		player1color = self.ui.color_menu
		player2color = self.ui.color_menu
		if match.winner == 1:
			player2color = self.ui.color_lighttext
		elif match.winner == 2:
			player1color = self.ui.color_lighttext
		elif is_next == True:
			player1color = self.ui.color_highlight
			player2color = self.ui.color_highlight

		self.ui.visiblebuttons.append(
			Button(self.ui.pygame, self.ui.mainArea).create(
				player1color,
				self.ui.color_darktext,
				self.ui.color_border,
				x,
				y,
				width,
				height,
				match.player1.name,
				self.drawBracket
			)
		)

		self.ui.visiblebuttons.append(
			Button(self.ui.pygame, self.ui.mainArea).create(
				player2color,
				self.ui.color_darktext,
				self.ui.color_border,
				x,
				y+height+5,
				width,
				height,
				match.player2.name,
				self.drawBracket
			)
		)



	def makeMatches(self):
		"""
		Appends a match to the Tournament object for each player belonging to the Tournament object.

		:param self: A reference to the Tournament object itself
		:return: returns nothing
		"""

		while len(self.players) > 1:
			self.matches.append(TournamentGame(self.players.pop(), self.players.pop()))


	def setWinner(self, player):
		"""
		Appends the current winners to a list belonging to the Tournament object which contains the players advancing to the next round.

		:param self: A reference to the Tournament object itself
		:param player: A reference to the player to be appended to the list of winners
		:return: returns nothing
		"""

		self.matches[self.currentGame-1].setWinner(player)
		if player == 1:
			self.players.append(self.matches[self.currentGame-1].player1)
		else:
			self.players.append(self.matches[self.currentGame-1].player2)

		print("We have a winner...")
		print(self.players)




