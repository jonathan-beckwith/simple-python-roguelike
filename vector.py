import math

def makeUniqueList(array):
	tuples = set([(x.x, x.y) for x in array])
	for x, y in tuples:
		yield Vector(x, y)

class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def distance(self, other):
		return math.sqrt(
			(self.x - other.x)**2 +
			(self.y - other.y)**2
		)

	def __str__(self):
		return "Vector({0}, {1})".format(self.x, self.y)

if __name__ == '__main__':
	import unittest

	class TestVectors(unittest.TestCase):
	
		def testMakeUniqueList(self):
			test_list = [
				Vector(1, 1),
				Vector(2, 2),
				Vector(2, 2),
				Vector(2, 2)
			]

			self.assertEqual(len([x for x in makeUniqueList(test_list)]), 2)
	unittest.main()