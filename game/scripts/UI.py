import scripts.gameHandler as gameHandler
import bge.logic as logic

class UI(gameHandler.Game):
	def __init__(self, fileName):
		gameHandler.Game.__init__(self, fileName)

		self.scene = logic.getCurrentScene()
		self.mapSquaresBuffer = []

	def showMap(self):
		pdb.set_trace()
		for x,lignes in enumerate(self.map):
			for y,square in enumerate(lignes):
				obj = None
				if square[0] == "sea":
					obj = self.scene.addObject("sea")
				elif square[0] == "ground":
					obj = self.scene.addObject("ground")
				else:
					continue
				self.mapSquaresBuffer.append(obj)
				obj.position[0] = x
				obj.position[1] = y
