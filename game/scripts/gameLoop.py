import bge.logic as logic


obj = logic.getCurrentController().owner
def main():
	if "GameStarted" in obj:
		obj["EventsHandler"].update()
