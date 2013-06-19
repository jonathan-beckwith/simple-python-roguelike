import math

class MonsterStats(object):
	def __init__(self):
		self.LVL = 1
		self.STR = 5
		self.MAG = 5
		self.VIT = 5
		self.AGI = 5
		self.SPR = 5

		self.calculateSecondaryStats()


	def calculateSecondaryStats(self):
		self.HP = 30 + self.VIT*20 + self.LVL*4
		self.MP =  math.floor((self.SPR + self.LVL) / 2)
		self.AP = self.STR * 2
		self.MAP = self.MAG * 2
		self.strength_multiplier = 1 + math.floor(self.STR / 100)
		self.magic_multiplier = 1 + math.floor(self.MAG / 100)
		self.accuracy = 5 + math.floor(self.AGI / 5)
		self.magic_accuracy = 5 + math.floor(self.MAG / 5)
		self.evade = 25 + math.floor(self.AGI / 5)
		self.resist = 25 + math.floor(self.VIT / 10) + math.floor(self.SPR / 10)
		self.critical = 98 - math.floor(self.AGI / 15)
		self.speed = 10 + math.floor(self.AGI / 15) + math.floor(self.LVL / 10)
		self.max_tech = 5 + math.floor(self.MAG / 2)
		pass

class Monster(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.health = 100
		self.sprite = None
		self.zindex = 0
		self.blocker = True

	def draw(self):
		self.sprite.x = self.x*32
		self.sprite.y = self.y*32
		self.sprite.draw()
	pass
