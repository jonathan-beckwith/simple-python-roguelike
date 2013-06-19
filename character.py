from armor import ArmorClass
from weapons import WeaponClass

import math

LVL_TABLE = [
	0, 50, 200, 450, 800, 1250, 1800, 2450, 3200, 4050, 5000, 6050, 7200, 8450, 
	9800, 11250, 12800, 14450, 16200, 18050, 20000, 22050, 24200, 26450, 28800, 
	31250, 33800, 36450, 39200, 42050, 45000, 48050, 51200, 54450, 57800, 61250,
	64800, 68450, 72200, 76050, 80000, 84050, 88200, 92450, 96800, 101250, 
	105800, 110450, 115200, 120050, 125000, 130050, 135200, 140450, 145800, 
	151250, 156800, 162450, 168200, 174050, 180000, 186050, 192200, 198450,
	204800, 211250, 217800, 224450, 231200, 238050, 245000, 252050, 259200,
	266450, 273800, 281250, 288800, 296450, 304200, 312050, 320000, 328050,
	336200, 344450, 352800, 361250, 369800, 378450, 387200, 396050, 405000,
	414050, 423200, 432450, 441800, 451250, 460800, 470450, 480200
]


class CharacterStats(object):
	def __init__(self, armorClass=ArmorClass.BALANCED, weaponClass=WeaponClass.DAGGER):
		#Armor and Weapon Class
		self.armorClass = armorClass
		self.weaponClass = weaponClass

		self.LVL = 1
		self.XP = 0

		#Primary Stats
		self.STR = 3
		self.MAG = 3
		self.VIT = 3
		self.AGI = 3
		self.SPR = 3
		self.stat_points = 25

		#Secondary Stats
		self.calculateSecondaryStats()

	def gainXP(self, XP):
		self.XP += XP;
		if self.XP >= LVL_TABLE:
			self.levelUp()

	def levelUp(self):
		self.stat_points += 3
		self.calculateSecondaryStats()		

	def calculateSecondaryStats(self):
		self.HP = 75 + self.VIT*5 + self.LVL*4
		self.MP = 5 + self.SPR + math.floor(self.LVL / 2)
		self.AP = 0 + self.STR
		self.MAP = 0 + self.MAG
		self.strength_roll = 1 + math.floor(self.STR / 100)
		self.magic_roll = 1 + math.floor(self.MAG / 100)
		self.accuracy = 5 + math.floor(self.AGI / 5)
		self.magic_accuracy = 5 + math.floor(self.MAG / 5)
		self.evade = 25 + math.floor(self.AGI / 5)
		self.resist = 25 + math.floor(self.VIT / 10) + math.floor(self.SPR / 10)
		self.critical = 98 - math.floor(self.AGI / 15)
		self.speed = 10 + math.floor(self.AGI / 15) + math.floor(self.LVL / 10)
		self.max_tech = 5 + math.floor(self.MAG / 2)

	def __str__(self):
		return """
		#Armor and Weapon Class
		armorClass = {armorClass}
		weaponClass = {weaponClass}

		LVL = {LVL}
		XP = {XP}

		#Primary Stats
		STR = {STR}
		MAG = {MAG}
		VIT = {VIT}
		AGI = {AGI}
		SPR = {SPR}
		stat_points = {stat_points}

		#Secondary Stats
		HP = {HP}
		MP = {MP}
		AP = {AP}
		MAP = {MAP}
		strength_roll = {strength_roll}
		magic_roll = {magic_roll}
		accuracy = {accuracy}
		magic_accuracy = {magic_accuracy}
		evade = {evade}
		resist = {resist}
		critical = {critical}
		speed = {speed}
		max_tech = {max_tech}
		""".format(**self.__dict__)

if __name__ == '__main__':
	a = Character()
	a.STR = 8
	a.MAG = 8
	a.VIT = 8
	a.AGI = 8
	a.SPR = 8
	a.calculateSecondaryStats()
	print(a)