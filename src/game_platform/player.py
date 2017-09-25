import abc

class Player(metaclass=abc.ABCMeta)
	"""
	Interface for player classes. 
	"""
	
	@abc.abstractmethod
	def isHuman(self):
		pass
	
	@abc.abstractmethod
	def play(self, state):
		pass


class Human(Player):
	def __init__(self, name):
		self.name = name

	def isHuman(self):
		return true

	def play(self, state):
		pass

class Computer(Player):
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def isHuman(self):
		return false

	def play(self, state):
		pass