import bge.events as events
import bge.logic as logic
import bge.render as render

#If the mouse is pressed:
def isPressedM(event):
	return logic.KX_INPUT_JUST_ACTIVATED in logic.mouse.inputs[event].queue
#If the keyboard is pressed:
def isPressedK(event):
	return logic.KX_INPUT_JUST_ACTIVATED in logic.keyboard.inputs[event].queue
#The same, but triggered every frame if only activated:
def isActivatedM(event):
	return logic.KX_INPUT_ACTIVE in logic.mouse.inputs[event].status
def isActivatedK(event):
	return logic.KX_INPUT_ACTIVE in logic.keyboard.inputs[event].status

#The GameEvents class handle the events from the player, and then trigger action in the core game class
class EventsHandler:
	def __init__(self, game):
		self.mouse = logic.mouse
		self.keyboard = logic.keyboard
		self.scene = logic.getCurrentScene()

		#An instance of the core game class:
		self.game = game
		#The orthographic scale of the camera
		self.orthoScale = 16

		#The cam tracer is the object used to manipulate the position of the camera
		self.camTracer = self.scene.objects["camTracer"]

		logic.mouse.position = (0.5, 0.5)

	def update(self):
		# Mouse events:
		mousePosX,mousePosY = logic.mouse.position

		if mousePosX >= .9:
			if mousePosX > 1:
				mousePosX = 1
			self.camTracer.applyMovement((.15, 0, 0), True)
		elif mousePosX <= .1:
			if mousePosX < 0:
				mousePosX = 0
			self.camTracer.applyMovement((-.15, 0, 0), True)
		if mousePosY <= .1:
			if mousePosY < 0:
				mousePosY = 0
			self.camTracer.applyMovement((0, .15, 0), True)
		elif mousePosY >= .9:
			if mousePosY > 1:
				mousePosY = 1
			self.camTracer.applyMovement((0, -.15, 0), True)

		# Update the screen with the current position of the mouse on the board
		tilePos = [0, 0]
		tilePos[0] = round(self.camTracer.position[0] + (1-mousePosX)*self.orthoScale-self.orthoScale/2, 0)
		tilePos[1] = round(self.camTracer.position[1] + ((mousePosY)*self.orthoScale-self.orthoScale/2)*(render.getWindowHeight() / render.getWindowWidth()), 0)
		obj = self.scene.objects["carre"]
		#obj.position[0] = tilePos[0]-self.camTracer.position[0]
		#obj.position[1] = tilePos[1]-self.camTracer.position[1]
