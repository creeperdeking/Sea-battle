# Ce sentiment... De paix, et d'amour, si pur.... Est-il possiblede vivre avec lui?
# Les conseils de cedric villani:
#	Etre toujours en mouvement
#	Se laisser guider par sa chance

import pdb
import scripts.utils as utils

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

		size = utils.Position([int(mapSizeStr[0]), int(mapSizeStr[1])])

		self.map = [["sea" for i in range(size.x)] for j in range(size.y)]

		#
		#Synthaxe du fichier:
			#1,2 land
		for i in content[1:-1]:
			parties = i.strip().split(" ")
			coordinates = parties[0].strip().split(',')
			#pdb.set_trace()
			self.map[int(coordinates[0])][int(coordinates[1])] = [parties[1]]

	def updateTerrain():
		print()
