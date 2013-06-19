
class Rectangle(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	pass

class QuadTree(object):
	MAX_OBJECTS = 10
	MAX_LEVELS = 5

	def __init__(self, bounds, level=0):
		self.level = level
		self.bounds = bounds
		self.nodes = []
		self.objects = []
		pass

	def clear(self):
		self.objects = []
		for node in self.nodes:
			node.clear()
		self.nodes = []
		pass

	def split(self):
		x = self.bounds.x
		y = self.bounds.y
		width = self.bounds.width / 2
		height = self.bounds.height / 2
		level = self.level + 1

		self.nodes[0] = QuadTree(level, Rectangle(x + width, y + height, width, height))
		self.nodes[1] = QuadTree(level, Rectangle(x,         y + height, width, height))
		self.nodes[2] = QuadTree(level, Rectangle(x + width, y,          width, height))
		self.nodes[3] = QuadTree(level, Rectangle(x,         y,          width, height))

	def getIndex(self, rect):
		index = -1
		bounds = self.bounds
		midx = bounds.x + (bounds.width / 2)
		midy = bounds.y + (bounds.height / 2)

		topQuad = rect.y < midy and rect.y + rect.height < midy
		bottomQuad = rect.y > midy

		if rect.x < midx and rect.x + rect.width < midx:
			if topQuad:
				index = 1
			elif bottomQuad:
				index = 2
		elif rect.x > midx:
			if topQuad:
				index = 0
			elif bottomQuad:
				index = 3