import abc
import random
import math
import time
import sys

sys.path.insert(0, '../game_engine')
from game_engine import game_engine

class Player(metaclass=abc.ABCMeta):
	"""
	Abstract interface for player classes that serves as a meta class.
	"""

	@abc.abstractmethod
	def isHuman(self):
		"""
		Abstract method that defines an "isHuman" function for Player objects, to be defined in subclasses.

		:param self: A reference to the Player object itself
		"""
		pass

	@abc.abstractmethod
	def play(self, state,currentplayer):
		"""
		Abstract method that defines a "play" function for Player objects, to be defined in subclasses.

		:param self: A reference to the Player object itself
		:param currentplayer: A reference to whom the currentplayer is
		:param state: A variable containing whatever state to use in subclass-defined versions of this method
		"""
		pass


class Human(Player):
	"""
	Human is a type of Player class, used to represent a human player in the application.
	"""
	def __init__(self, name):
		"""
		Construct a new Human object.

		:param self: A reference to the Human object itself
		:param name: A name given to the Human object
		:return: returns nothing
		"""
		self.name = name
		self.human = True
		self.move = -1

	def isHuman(self):
		"""
		Returns whether or not the Player object is a Human (true).

		:param self: A reference to the Human object itself
		:return: returns a boolean stating if the Player object is of type Human
		"""
		return self.human

	def play(self, state,currentplayer):
		"""
		Performs a given play

		:param self: A reference to the Human object itself
		:param state: A reference to the current game state
		:param currentplayer: A reference to whom the currentplayer is
		:return: returns an integer representing an index in the game board
		"""
		tentativeMove = self.move
		self.move = -1
		return tentativeMove

class Computer(Player):
	"""
	Computer is a type of Player class, used to represent a computer player in the application.
	"""
	def __init__(self, name, level):
		"""
		Construct a new Computer object.

		:param self: A reference to the Computer object itself
		:param name: A name given to the Computer object
		:param level: A difficulty level given to the Computer object
		:return: returns nothing
		"""
		self.name = name
		self.level = level
		self.human = False
		self.timer = None
		self.ai = game_engine(level)

	def isHuman(self):
		"""
		Returns whether or not the Player object is a Human (false).

		:param self: A reference to the Computer object itself
		:return: returns a boolean stating if the Player object is of type Human
		"""
		return self.human

	def play(self, state, currentplayer):
		"""
		Performs a given play

		:param self: A reference to the Human object itself
		:param state: A reference to the current game state
		:param currentplayer: A reference to whom the currentplayer is
		:return: returns the next AI move to make
		"""
		if(self.timer == None):
			self.timer = time.time()
			return -1
		else:
			if(time.time()-self.timer < 0.5):
				return -1
			else:
				self.timer = None

		return self.ai.makemove(state, currentplayer)