import datetime, random, pygame, sys, time
from pygame.locals import *
from button import Button
from centeredtext import centeredtext
from player_names import Playernames

def actionPrint():
	print("test")

class GameUI:
	"""
	GameUI is the main class for the Game User Interface
	"""
	def __init__(self):
		self.WINDOW_SIZE = width, height = 1280, 720
		self.TOP_RATIO = 2/7
		self.BOTTOM_RATIO = 5/7

		self.color_background = pygame.Color(83, 178, 162)
		self.color_menu = pygame.Color(247, 247, 247)
		self.color_border = pygame.Color(144, 148, 150)
		self.color_lighttext = pygame.Color(149, 152, 154)
		self.color_darktext = pygame.Color(74, 74, 74)

		pygame.init()

		self.playernames = []


		self.currentplayerEdit = 0;

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

		title = centeredtext("Tic Tac Toe", 0,0, 1280, 75, pygame, 100, self.color_lighttext)
		title.draw(self.secondaryArea, self.color_menu)

		self.border   = pygame.draw.line(
			self.screen,
			self.color_border,
			(0, self.screen.get_height()*self.TOP_RATIO),
			(self.screen.get_width(),
			self.screen.get_height()*self.TOP_RATIO),
			2
		)
		self.displayMainMenu()

	def checkButtonClick(self, pos):
		for button in self.visiblebuttons:
			offset = button.area.get_offset()
			if (button.box.collidepoint((pos[0]-offset[0]), (pos[1]-offset[1]))): button.action()
		# for button in self.visiblebuttons2:
		# 	offset = button.area.get_offset()
		# 	if (button.box.collidepoint((pos[0]-offset[0]), (pos[1]-offset[1]))): button.action(button.arg1, button.arg2)

	def tic(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN: self.checkButtonClick(pygame.mouse.get_pos())

		pygame.display.flip()

	def displayMainMenu(self):
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 200
		buttonHeight = 50

		self.visiblebuttons = (
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
		)

	def displayGame(self, player1, player2):
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50

		self.visiblebuttons = (
			(Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				100,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Back",
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
				"Forfit",
				self.displayMainMenu
			))
		)

	def displaySingelPlayer(self):
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50
		
		self.playernames = []
		
		self.playernames.append(self.askfornames.ask("Player 1"))
		self.playernames.append("Computer")
		self.displayGame(self.playernames[0], self.playernames[1])

	def displayTwoPlayer(self):
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50
		
		self.playernames = []
		self.playernames.append(self.askfornames.ask("Player 1"))
		self.playernames.append(self.askfornames.ask("Player 2"))
		self.displayGame(self.playernames[0], self.playernames[1])

	def displayCreateTournament(self):
		self.mainArea.fill(self.color_background)
		buttonHalfWidth = 150
		buttonHeight = 50
		
		self.playernames = []
		
		for n in range(8):
			self.playernames.append(self.askfornames.ask("Player " + str(n+1)))

		self.mainArea.fill(self.color_background)
		
		self.visiblebuttons = []
		
		x = 20;
		y = 20;

		for n in range(8):	
			y = y + 80

			if n % 2 == 0:
				x = 100
			else:
				y = y - 80
				x = 825

			if len(self.playernames[n]) != 0:
				self.visiblebuttons.append(
					Button(pygame, self.mainArea).create(
						self.color_menu,
						self.color_darktext,
						self.color_border,
						x,
						y,
						buttonHalfWidth*2.5,
						buttonHeight,
						self.playernames[n],
						self.displayMainMenu
					)
				)
			
		self.visiblebuttons.append(
			Button(pygame, self.mainArea).create(
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
		self.visiblebuttons.append(
			Button(pygame, self.mainArea).create(
				self.color_menu,
				self.color_darktext,
				self.color_border,
				900,
				450,
				buttonHalfWidth*2,
				buttonHeight,
				"Start Tournament",
				self.displayMainMenu
			)
		)
			




ui = GameUI()
while 1:
	ui.tic()
