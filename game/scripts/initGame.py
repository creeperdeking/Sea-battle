import bge.logic as logic

import scripts.UI as UI
import scripts.eventsHandler as eventsH

def main():
	obj = logic.getCurrentController().owner
	if not "Game" in obj:
		game = UI.UI(logic.expandPath("//map.map"))
		obj["Game"] = game
		game.showMap()
		obj["EventsHandler"] = eventsH.EventsHandler(game)
		obj["GameStarted"] = True
