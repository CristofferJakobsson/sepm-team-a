import datetime, random, pygame, sys, time
from pygame.locals import *
from button import Button
from centeredtext import centeredtext
#from board import Board
from player_names import Playernames
from tournament_tree import Tournament

import sys
sys.path.insert(0, '../game_platform')
from game_platform import Game
from player import Player, Human, Computer



def actionPrint():
    print("test")


class GameUI:
	"""
	GameUI is the main class for the Game User Interface
	"""
	def __init__(self):
		"""
		Construct a new GameUI object.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""

		self.pygame = pygame
		self.WINDOW_SIZE = width, height = 1280, 720
		self.TOP_RATIO = 2/7
		self.BOTTOM_RATIO = 5/7

		self.color_background 	= pygame.Color(83, 178, 162)
		self.color_menu 		= pygame.Color(247, 247, 247)
		self.color_border 		= pygame.Color(144, 148, 150)
		self.color_lighttext 	= pygame.Color(149, 152, 154)
		self.color_darktext 	= pygame.Color(74, 74, 74)
		self.color_darkgreen 	= pygame.Color(14,151,135)
		self.color_black 		= pygame.Color(0,0,0)
		self.color_highlight    = pygame.Color(83, 241, 162)

		pygame.init()

		self.playernames = []
		self.currentplayerEdit = 0

		pygame.display.set_caption("Tic Tac Toe")

		self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
		self.mainArea = self.screen.subsurface(
			self.screen.fill(
				self.color_background,
				pygame.Rect(
					0,
					self.screen.get_height()*self.TOP_RATIO,
					self.screen.get_width(),
					self.screen.get_height()*self.BOTTOM_RATIO
				)
			)
		)

		self.secondaryArea = self.screen.subsurface(
			self.screen.fill(
				self.color_menu,
				pygame.Rect(
					0,
					0,
					self.screen.get_width(),
					self.screen.get_height()*self.TOP_RATIO
				)
			)
		)
		self.askfornames  = Playernames(self.mainArea)
		self.renderTop("","", 1)
		self.border   = pygame.draw.line(
			self.screen,
			self.color_border,
			(0, self.screen.get_height()*self.TOP_RATIO),
			(self.screen.get_width(),
			self.screen.get_height()*self.TOP_RATIO),
			2
		)
		self.displayMainMenu()

	def renderTop(self,player1, player2, playing):
		"""
		Renders the top part of the screen when playing a game.

		:param self: A reference to the GameUI object itself
		:param player1: Player 1 in the active game
		:param player2: Player 2 in the active game
		:param playing: A value deciding which player is currently playing (1 == player1 etc.)
		:return: returns nothing
		"""
		buttonHalfWidth = 200
		buttonHeight = 50

		self.secondaryArea.fill(self.color_menu)

		title = centeredtext("Tic Tac Toe", 0,0, 1280, 75, pygame, 100, self.color_lighttext)
		title.draw(self.secondaryArea, self.color_menu)

		name1 = player1
		name2 = player2

		if isinstance(player1, Player):
			name1 = player1.name
		if isinstance(player2, Player):
			name2 = player2.name


		if len(name1) != 0:
			(Button(pygame, self.secondaryArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				100,
				100,
				buttonHalfWidth*2,
				buttonHeight,
				"X  " + name1,
				self.displaySingelPlayer
			))
			if playing == 1:
				box = pygame.Rect(100,150,400,5)
				self.secondaryArea.fill(self.color_background, box)

		if len(name2) != 0:
			(Button(pygame, self.secondaryArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				825,
				100,
				buttonHalfWidth*2,
				buttonHeight,
				"O  " + name2,
				self.displayTwoPlayer
			))
			if playing == -1:
				box = pygame.Rect(825,150,400,5)
				self.secondaryArea.fill(self.color_background, box)


	def checkButtonClick(self, pos):
		"""
		Check if the clicked screen-coordinates collide with existing buttons.

		:param self: A reference to the GameUI object itself
		:param pos: The position where the screen was clicked
		:return: returns nothing
		"""
		for button in self.visiblebuttons:
			offset = button.area.get_offset()
			if (button.box.collidepoint((pos[0]-offset[0]), (pos[1]-offset[1]))): button.action()

	def tic(self):
		"""
		A time-tic in the running game state.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if(pygame.mouse.get_pressed()[0]):
					if(hasattr(self, 'game')):
						if(self.game):
							self.game.click(pygame.mouse.get_pos())
					self.checkButtonClick(pygame.mouse.get_pos())

		if(hasattr(self, 'game')):
			if(self.game):
				self.game.gameTic()

		pygame.display.flip()

	def displayMainMenu(self):
		"""
		Displays the main menu of the GameUI object on the screen.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 200
		buttonHeight = 50

		self.game = None

		self.renderTop("","",1)
		self.visiblebuttons = [
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				self.WINDOW_SIZE[0]/2-buttonHalfWidth,
				50,
				buttonHalfWidth*2,
				buttonHeight,
				"Player vs Computer",
				self.displaySingelPlayer
			)),
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				self.WINDOW_SIZE[0]/2-buttonHalfWidth,
				110,
				buttonHalfWidth*2,
				buttonHeight,
				"Player vs Player",
				self.displayTwoPlayer
			)),
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				self.WINDOW_SIZE[0]/2-buttonHalfWidth,
				170,
				buttonHalfWidth*2,
				buttonHeight,
				"Player Tournament",
				self.displayCreateTournament
			)),
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				self.WINDOW_SIZE[0]/2-buttonHalfWidth,
				400,
				buttonHalfWidth*2,
				buttonHeight,
				"Exit",
				sys.exit
			))
		]

	def displayGame(self, player1, player2, tournamentgame = None):
		"""
		Displays a game-view on the screen.

		:param self: A reference to the GameUI object itself
		:param player1: Name of player 1
		:param player2: Name of player 2
		:param tournamentgame: A boolean determining whether the current game is a tournament game
		:return: returns nothing
		"""
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50
		backtext = "Back"
		if tournamentgame:
			backtext = "Quit Tournament"

		self.visiblebuttons = [
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				100,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				backtext,
				self.displayMainMenu
			)),
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				900,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Forfeit",
				self.playerForfeit
			))
		]
		if tournamentgame:
			print("This is a tournamentgame")
			self.game = Game(self, player1, player2, True, tournamentgame)
		else:
			self.game = Game(self, player1, player2)

		self.renderTop(player1, player2, self.game.currentplayer)

	def displaySingelPlayer(self):
		"""
		Displays the view for a singleplayer game (player versus computer)

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50

		self.playernames = []

		self.playernames.append(self.askfornames.ask("Player 1", self.playernames))
		self.playernames.append("Computer")
		computerdifficulty = -1
		while(computerdifficulty not in [1, 2, 3]):
			try:
				computerdifficulty = int(self.askfornames.ask("AI Dificculty (1-3)"))
			except ValueError:
				pass
		player1 = Human(self.playernames[0])
		if computerdifficulty == 3:
			lvl = "hard"
		elif computerdifficulty == 2:
			lvl = "normal"
		else:
			lvl = "easy"
		player2 = Computer(self.playernames[1], lvl)
		self.displayGame(player1, player2)

	def displayTwoPlayer(self):
		"""
		Displays the view for a multiplayer game (player versus player)

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50

		self.playernames = []
		self.playernames.append(self.askfornames.ask("Player 1", self.playernames))
		self.playernames.append(self.askfornames.ask("Player 2", self.playernames))

		player1 = Human(self.playernames[0])
		player2 = Human(self.playernames[1])

		self.displayGame(player1, player2)

	def displayCreateTournament(self):
		"""
		Displays the tournament creation view on the screen.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.mainArea.fill(self.color_background)
		self.visiblebuttons = []
		self.playernames = []
		numplayers = 0

		while(numplayers not in range(2,9)):
			try:
				numplayers = int(self.askfornames.ask("Number of players: (2-8)"))
			except ValueError:
				pass

		for n in range(numplayers):
			self.playernames.append(self.askfornames.ask("Player " + str(n+1), self.playernames))

		self.tournament = Tournament(self, self.playernames)

		self.displayCurrentTournament()



	def displayCurrentTournament(self):
		"""
		Displays the tournament current active tournament.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.renderTop("","", 1)
		buttonHalfWidth = 150
		buttonHeight = 50
		self.mainArea.fill(self.color_background)
		self.visiblebuttons = []
		self.tournament.drawBracket()
		if (self.tournament.currentGame == len(self.tournament.matches)):
			self.tournament.drawTournamentWinScreen(self.tournament.getNextMatch())
			return

		self.visiblebuttons.append(
			Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				100,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Quit Tournament",
				self.displayMainMenu
			)
		)
		self.visiblebuttons.append(
			Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				900,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Play",
				self.displayTournamentGame
			)
		)

	def playerForfeit(self):
		"""
		Forfeits the game for the current player.

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		if(hasattr(self, 'game')):
			if(self.game):
				self.game.playerForfeit()

	def displayTournamentGame(self, replaygame=False):
		"""
		Displays the current Tournament game.

		:param self: A reference to the GameUI object itself
		:param replaygame: A boolean deciding whether the current game should be replayed
		:return: returns nothing
		"""
		self.visiblebuttons = []
		self.mainArea.fill(self.color_background)
		if replaygame:
			crap, tournamentGame = self.tournament.getCurrentMatch()
		else:
			crap, tournamentGame = self.tournament.getNextMatch()
		print(tournamentGame)
		self.displayGame(tournamentGame.player1, tournamentGame.player2, tournamentGame)

	def removeButton(self, buttontext):
		"""
		Removes a button with the given buttontext

		:param buttontext: Text that is used to find the button to remove
		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		print("Should remove " + buttontext + " button")
		for i in range(0,len(self.visiblebuttons)):
			print("Currently looking at button " + self.visiblebuttons[i].text)
			if (self.visiblebuttons[i].text==buttontext):
				break

	def putOnlyBackButton(self):
		"""
		Displays the back button

		:param self: A reference to the GameUI object itself
		:return: returns nothing
		"""
		self.visiblebuttons = []
		buttonHalfWidth = 150
		buttonHeight = 50
		self.mainArea.fill(self.color_background)
		self.visiblebuttons.append(
			Button(self.pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				100,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Back",
				self.displayMainMenu
			)
		)

ui = GameUI()
while 1:
	ui.tic()
