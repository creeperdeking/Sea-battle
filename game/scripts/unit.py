"""
information:
	le point(0,0) de la carte est le point en haut a droite
	la coordonnée x est la coordonée de largeur
	la coordonnée y est la coordonée de longueur


donnée manquente:
"""

import scripts.utils as utils

def generate_map(largueur_carte,longueur_carte):
	"""renvoie une carte pleine d'eau (a finir)"""
	carte=[["mer" for i in range(largueur_carte)] for j in range(longueur_carte)]
	return(carte)

class unite:
	def __init__(self):
		self.type = "mer"
		self.point_vie = 0
		self.point_deplacement = 0
		self.porté_d_attaque = 0

		self.point_attaque = 0

		self.zone_vision_mer = 0
		self.zone_vision_terre = 0
		self.zone_vision_air = 0

		self.position = utils.Position([0,0])
		self.position.x = 0
		self.position.y = 0

	def posibiliter_deplacement(self,carte):
		"""fonction qui renvois la liste des cases accessible"""
		accessibe=[]
		for x in range(-self.point_deplacement,self.point_deplacement+1):
			for y in range(-self.point_deplacement,self.point_deplacement+1):
				#parcour tout les cases a porter de deplacement et test leurs types si elles existent
				if self.position.x+x >= 0 and self.position.y+y >= 0 and ( self.type == "air" or carte[self.position.x+x][self.position.y+y][0]==self.type ):
					accessible.append([self.position.x+x,self.position.y+y])
		return(accessible)

	def posibiliter_attaque(self,carte):
		"""fonction qui renvois la liste des cases attaquable""" #work in progres
		attaquable=[]
		for x in range(-self.porté_d_attaque,self.porté_d_attaque+1):
			for y in range(-self.point_deplacement,self.point_deplacement+1):
				#condition a faire
				if self.position.x+x >= 0 and self.position.y+y >= 0 and ( self.type == "air" or carte[self.position.x+x][self.position.y+y][0]==self.type ):
					attaquable.append([self.position.x+x,self.position.y+y])
		return(attaquable)
