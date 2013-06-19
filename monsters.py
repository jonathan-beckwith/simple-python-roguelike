from monster import Monster, MonsterStats
from weapons import Weapon
from player import Player
import game_map

from resources import monsters
from pyglet import sprite
from vector import Vector
import combat

class Rat(Monster):

	def __init__(self):
		self.x = 12
		self.y = 12
		self.vision = 3
		self.tile_index = -1
		self.sprite = sprite.Sprite(
			img=monsters[11,0],
			x=320,
			y=320
		)
		self.hunger = 0
		self.target = Vector(self.x, self.y)
		self.stats = MonsterStats()
		self.weapon = Weapon({
			'class': "teeth",
			'name': "Teeth",
			'LVL': 1,
			'AD': 3,
			'MD': 3,
			'special': None,
			'description': "Rats attack using their teeth."
		})
		self.blocker = True
		self.zindex = 100
		self.SP = 32

	def attack(self, target):
		attack_result = combat.attack(self, target)
		print(attack_result)
		target.HP -= attack_result.damage
		self.hunger += 1

	def lookForFood(self):
		for x in game_map.getEntitiesInTiles(game_map.getAdjacentTiles(self, self.vision)):
			if hasattr(x, 'edible'):
				self.target = x

	def removeFromMap(self):
		game_map.removeEntity(self)

	def addToMap(self):
		game_map.addEntity(self)

	def get_target(self):
		for x in game_map.getEntitiesInPositions(game_map.getAdjacentTiles(self, self.vision)):
			if type(x) is Player:
				self.target = Vector(x.x, x.y)

		for x in game_map.getEntitiesInPositions(game_map.getAdjacentTiles(self, 2)):
			if type(x) is Player:
				self.attack(x)

	def move(self): 
		if self.target == Vector(self.x, self.y):
			print("Rat is resting.")
			return

		self.removeFromMap()

		if self.hunger > 0:
			self.lookForFood()

		directions = [
			Vector(0, 1),
			Vector(0, -1),
			Vector(1, 0),
			Vector(-1, 0)
		]

		pos = Vector(self.x, self.y)

		blocked = True

		distance = pos.distance(self.target)
		for direction in directions:
			test_pos = direction + pos
			if game_map.blocked(test_pos) is not True:
				if test_pos.distance(self.target) < distance:
					pos = test_pos
					distance = pos.distance(self.target)

		self.x = pos.x
		self.y = pos.y
		self.SP -= 8

		self.addToMap()

	def update(self):
		self.get_target()

		if self.SP > 16:
			self.move()

		self.SP += 3
		print('rat SP:', self.SP)
		
		for x in game_map.getEntitiesInTiles(game_map.getAdjacentTiles(self, 1)):
			if type(x) is Player:
				self.attack(x)

			if hasattr(x, 'edible') and self.hunger > 5:
				self.eat(x)
