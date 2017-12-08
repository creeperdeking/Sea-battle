import scripts.utils as utils


class Unite:
	def __init__(self):
		self.type = "sea"
		self.point_vie = 0
		self.point_deplacement = 0
		self.porté_d_attaque = 0
		self.point_attaque = 0

		self.zone_vision_mer = 0
		self.zone_vision_terre = 0
		self.zone_vision_air = 0
		self.zone_vision_sous_marine = 0

		self.position = utils.Position([0,0])

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
		"""fonction qui renvois la liste des cases attaquable""" 
		attaquable=[]
		for x in range(-self.porté_d_attaque,self.porté_d_attaque+1):
			for y in range(-self.porté_d_attaque,self.porté_d_attaque+1):
				#condition a faire
				if self.position.x+x >= 0 and self.position.y+y >= 0:
					attaquable.append([self.position.x+x,self.position.y+y])
		return(attaquable)

        def attaque(self,ennemi):
                """fonction qui calcule les degats"""
                ennemi.point_vie -= self.point_attaque


class UnitesTerrestre(Unite):
        def __init__(self):
                Unite.__init__(self)
                self.zone_vision_mer = 3
		self.zone_vision_terre = 2
		self.zone_vision_air = 2
		self.zone_vision_sous_marine = 0

class UnitesMaritime(Unite):
        def __init__(self):
                Unite.__init__(self)
                self.zone_vision_mer = 3
		self.zone_vision_terre = 2
		self.zone_vision_air = 4
		self.zone_vision_sous_marine = 1

class UnitesSousMarine(Unite):
        def __init__(self):
                Unite.__init__(self)
                self.zone_vision_mer = 2
		self.zone_vision_terre = 1
		self.zone_vision_air = 0
		self.zone_vision_sous_marine = 3

class UnitesAeriennes(Unite):
        def __init__(self):
                Unite.__init__(self)
                self.zone_vision_mer = 5
		self.zone_vision_terre = 3
		self.zone_vision_air = 5
		self.zone_vision_sous_marine = 0

class InfanterieLourde(UnitesTerrestre):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 1
		self.point_deplacement = 2
		self.porté_d_attaque = 1
		self.point_attaque = 1

class Tanks(UnitesTerrestre):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 2
		self.point_deplacement = 2
		self.porté_d_attaque = 2
		self.point_attaque = 2

class Destroyes(UnitesMaritime):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 2
		self.point_deplacement = 5
		self.porté_d_attaque = 2
		self.point_attaque = 2

class Croiseurs(UnitesMaritime):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 3
		self.point_deplacement = 3
		self.porté_d_attaque = 4
		self.point_attaque = 3

class Cuirasses(UnitesMaritime):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 5
		self.point_deplacement = 2
		self.porté_d_attaque = 5
		self.point_attaque = 4

class PorteAvions(UnitesMaritime):
        def __init__(self):
                UnitesTerrestre.__init__(self)
                self.point_vie = 5
		self.point_deplacement = 3
		self.porté_d_attaque = 2
		self.point_attaque = 1

class SousMarins(UnitesSousMarine):
        def __init__(self):
                UnitesSousMarine.__init__(self)
                self.point_vie = 3
		self.point_deplacement = 2
		self.porté_d_attaque = 2
		self.point_attaque = 3

class Avions(UnitesAeriennes):
        def __init__(self):
                UnitesAeriennes.__init__(self)
                self.point_vie = 1
		self.point_deplacement = 10
		self.porté_d_attaque = 1
		self.point_attaque = 2
