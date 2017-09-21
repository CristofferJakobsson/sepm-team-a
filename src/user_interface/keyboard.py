

class keyboard:
	def __init__(self, textbuffer):
		self.textbuffer = textbuffer
	def a(self):
		self.append("a")
	def b(self):
		self.append("b")
	def c(self):
		self.append("c")
	def d(self):
		self.append("d")
	def e(self):
		self.append("e")
	def f(self):
		self.append("f")
	def g(self):
		self.append("g")
	def h(self):
		self.append("h")
	def i(self):
		self.append("i")
	def j(self):
		self.append("j")
	def k(self):
		self.append("k")
	def l(self):
		self.append("l")
	def m(self):
		self.append("m")
	def n(self):
		self.append("n")
	def o(self):
		self.append("o")
	def p(self):
		self.append("p")
	def q(self):
		self.append("q")
	def r(self):
		self.append("r")
	def s(self):
		self.append("s")
	def t(self):
		self.append("t")
	def u(self):
		self.append("u")
	def v(self):
		self.append("v")
	def w(self):
		self.append("w")
	def x(self):
		self.append("x")
	def y(self):
		self.append("y")
	def z(self):
		self.append("z")
	def back(self):
		self.textbuffer = self.textbuffer[:-1]
		return self.textbuffer

	def append(self, char):
		self.textbuffer += char
		return self.textbuffer
