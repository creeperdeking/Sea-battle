"""
information:
	le point(0,0) de la carte est le point en haut a droite
	la coordonnée x est la coordonée de largeur
	la coordonnée y est la coordonée de longueur


donnée manquente:
"""

import pdb
import scripts.utils as utils
import scripts.unit as unit

class Game:
	"""A class designed to handle the behavior of the game, independently from events or graphical interface"""
	def __init__(self, fileName):
		print("Initialising game")

		self.map = [[]]
		self.loadMapFromFile(fileName)

		self.tour = 1

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

	def generate_map(largueur_carte,longueur_carte):
                """renvoie une carte pleine d'eau (a finir)"""
                carte=[["sea" for i in range(largueur_carte)] for j in range(longueur_carte)]
                return(carte)
        
        def tourSuivant(self):
                self.tour += 1

class Player:
        def __init__(self):
                self.nom = "random"
                self.point = 0
                self.unite = []

        def calculPoint(self):
                self.point = 0
                for bateau in self.unite:
                        self.point += bateau.point_vie
                
