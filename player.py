from pyglet import sprite

import resources
import character
from vector import Vector

import game_map

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class Player(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.sprite = sprite.Sprite(
			img=resources.player_image,
			x=0,
			y=0
		)
		self.direction = None
		self.stats = character.CharacterStats()
		self.HP = self.stats.HP
		self.SP = self.stats.speed
		self.blocker = True
		self.zindex = 100

	def update(self):
		if self.direction is not None:
			game_map.removeEntity(self)

			pos = Vector(self.x, self.y)
			if self.direction is NORTH:
				pos.y += 1
				pass
			elif self.direction is SOUTH:
				pos.y -= 1
				pass
			elif self.direction is EAST:
				pos.x += 1
				pass
			elif self.direction is WEST:
				pos.x -= 1
				pass

			if game_map.blocked(pos) is False:
				self.x = pos.x
				self.y = pos.y

			game_map.addEntity(self)
			self.direction = None
		pass

	def draw(self):
		self.sprite.x = self.x*32
		self.sprite.y = self.y*32
		self.sprite.draw()