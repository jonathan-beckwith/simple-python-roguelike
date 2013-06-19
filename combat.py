import random
import math

def log(message):
	print(message)

class AttackResult(object):
	def __init__(self):
		self.status = "Miss"
		self.damage = 0

	def __str__(self):
		return "{0}: {1}".format(self.status, self.damage)

def damage(attacker, multiplier):
	return math.floor(((random.random() * attacker.weapon.AD) * 5) + attacker.stats.AP)*multiplier

def attack(attacker, defender):
	hit_chance = math.floor(random.random() * 101)
	
	damage_multiplier = 1
	attack_result = AttackResult()

	if hit_chance > 90 or hit_chance + attacker.stats.accuracy > defender.stats.evade:
		attack_result.status = "Hit"
		if hit_chance >= attacker.stats.critical:
			attack_result.status = "Critical"
			damage_multiplier = 2

		attack_result.damage = damage(attacker, damage_multiplier)

	return attack_result

class Combat(object):
	def __init__(self, entities):
		self.entities = entities

	def tick(self):
		pass

if __name__ == '__main__':
	import unittest

	class Weapon(object):
		def __init__(self):
			self.AD = 3
			self.AP = 15
		def getDamage(self):
			return math.floor(random.random() * self.power)

	class Stats:
		evade = 50
		accuracy = 50
		critical = 98
		AP = 15

	class Entity(object):
		def __init__(self):
			self.stats = Stats()
			self.weapon = Weapon()

		def __str__(self):
			return "evade {0}, accuracy {1}".format(self.stats.evade, self.stats.accuracy)

	class test_combat(unittest.TestCase):
		def test_attack(self):
			for i in range(100):
				attacker = Entity()
				defender = Entity()
				log(attack(attacker, defender))

	unittest.main()