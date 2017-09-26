import abc

class Player(metaclass=abc.ABCMeta):
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
		self.human = True

	def isHuman(self):
		return self.human

	def play(self, state):
		pass

class Computer(Player):
	def __init__(self, name, level):
		self.name = name
		self.level = level
		self.human = False

	def isHuman(self):
		return self.human

	def play(self, state):
		pass