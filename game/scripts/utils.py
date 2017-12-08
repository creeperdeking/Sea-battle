# A simple class to represent a 2D position:
class Position:
	def __init__(self, liste=[0,0]):
		self.x = int(liste[0])
		self.y = int(liste[1])

	def vect(self):
		return [self.x, self.y]

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)
