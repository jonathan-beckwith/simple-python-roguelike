import resources

#Just a blue overlay that can be added to tiles for various purposes
class LineOfSight(object):
	def __init__(self, x, y):
		self.tile_index = -1
		self.sprite = resources.blue_overlay
		sprite.x = x
		sprite.y = y
		self.x = x
		self.y = y
		self.zindex = -1
		self.blocker = False

	def draw(self):
		self.sprite.draw()
		pass