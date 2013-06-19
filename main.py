from pyglet import app
from pyglet import window
from pyglet import clock
from pyglet import graphics
from pyglet import resource
from pyglet import sprite
from pyglet import image
from pyglet import text
from pyglet.window import key

from math import sqrt

import random

from uuid import uuid4

from vector import Vector
import vector

import game_map

from player import Player

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

fps_display = clock.ClockDisplay()
game_window = window.Window()

player = Player()

health_ui = text.Label(
	text = "Health: -",
	x=0,
	y=475,
	anchor_y='top'
)
stamina_ui = text.Label(
	text = "Stamina: -",
	x=0,
	y=450,
	anchor_y='top'
)

import combat
from weapons import Weapon

from monsters import Rat
rat = Rat()

def load():
	game_map.addEntity(rat)
	game_map.addEntity(player)
	pass

def update(dt):
	player.update()
	rat.update()
	health_ui.text = "Health: {0}".format(player.HP)
	stamina_ui.text = "Stamina: {0}".format(player.SP)
	pass

@game_window.event
def on_draw():
	game_window.clear()
	game_map.draw()
	fps_display.draw()
	health_ui.draw()
	stamina_ui.draw()
	pass

@game_window.event
def on_key_press(symbol, modifier):
	
	if symbol == key.UP:
		player.direction = NORTH
	elif symbol == key.DOWN:
		player.direction = SOUTH
	elif symbol == key.LEFT:
		player.direction = WEST
	elif symbol == key.RIGHT:
		player.direction = EAST
	pass

	update(0)

def main():
	#clock.schedule(update)
	load()
	app.run()
	pass

if __name__ == '__main__':
	main()