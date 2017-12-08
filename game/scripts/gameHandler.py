import bge.logic as logic
# Ce sentiment... De paix, et d'amour, si pur.... Est-il possiblede vivre avec lui?
# LEs conseils de cedric villani:
#	Etre toujours en mouvement
#	Se laisser guider par sa chance

class Game:
	"""A class designed to handle the comportement of the game, independently from events or graphical interface"""
	def __init__(self, fileName):
		print("Initialising game")

		self.map = [[]]
		self.loadMapFromFile(fileName)


	def loadMapFromFile(self, filePath):
		f = open(filePath, 'r')
		content = f.readlines()
		mapSizeStr = content[0].strip().split(',')
		size = [int(mapSizeStr[0]), int(mapSizeStr[1])]

		for i in range(int(size[0])):
			a = []
			for j in range(int(size[1])):
				a.append("")
			self.map.append(a)

		#Synthaxe du fichier:
			#1,2 land
		for i in content:
			parties = i.split(" ")
			coordinates = parties[0].split(',')
			self.map[(coordinates[0])][(coordinates[1])] = [parties[1]]

	def updateTerrain():
		print()
