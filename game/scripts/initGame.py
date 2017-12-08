import bge.logic as logic

import scripts.gameHandler as gameH
import scripts.eventsHandler as eventsH

def main():
	obj = logic.getCurrentController().owner
	game = gameH.Game(logic.expandPath("//map.map"))
	obj["Game"] = game
	obj["EventsHandler"] = eventsH.EventsHandler(game)
	obj["GameStarted"] = True
