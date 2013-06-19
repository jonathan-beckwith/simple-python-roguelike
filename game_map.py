from pyglet import image

import resources
import vector
from vector import Vector

textures = resources.map_tiles

class Terrain(object):
	pass

class Grass(Terrain):
	def __init__(self):
		self.texture = 153
		self.blocked = False
	pass

class Wall(Terrain):
	def __init__(self):
		self.texture = 143
		self.blocked = True

class Tile(object):
	def __init__(self, terrain, pos):
		self.terrain = terrain
		self.entities = []
		self.blocked = self.terrain.blocked
		self.x = pos.x
		self.y = pos.y

	def removeEntity(self, entity):
		self.blocked = self.terrain.blocked
		
		entity_count = 0

		self.entities[entity.tile_index] = None
		entity.tile_index = -1

		for x in self.entities:
			if hasattr(x, 'blocker') and x.blocker == True:
				self.blocked = True
				return
			if x is not None:
				entity_count += 1

		if entity_count == 0:
			self.entities = []

	def addEntity(self, entity):
		entity.tile_index = len(self.entities)
		self.entities.append(entity)
		if hasattr(entity, 'blocker') and entity.blocker is True:
			self.blocked = True

	def draw(self):
		pass
	pass

#TODO: Load from a file here.
raw_data = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

data = []
raw_data.reverse()
[x.reverse for x in raw_data]
grass = Grass()
wall = Wall()
for row, x in enumerate(raw_data):
	row_arr = []
	for col, y in enumerate(x):
		pos = Vector(row, col)
		if y == 0:
			row_arr.append(Tile(grass, pos))
		else:
			row_arr.append(Tile(wall, pos))
	data.append(row_arr)


def draw_radius(pos, distance):
	[draw_tile(tile) for tile in getAdjacentTiles(pos, distance)]

def draw():
	[[draw_tile(tile) for tile in row] for row in data]

def draw_tile(tile):
	textures[tile.terrain.texture].blit(tile.x*32, tile.y*32)
	[x.draw() for x in sorted(tile.entities, key=lambda entity: getattr(entity, 'zindex', 0)) if x is not None]
	pass


def addEntity(entity):
	data[entity.x][entity.y].addEntity(entity)
	pass

def removeEntity(entity):
	data[entity.x][entity.y].removeEntity(entity)
	pass

def blocked(pos):
	return data[pos.x][pos.y].blocked

def getTiles(array):
	for x in array:
		yield data[x.x][x.y]

def getAdjacentTiles(entity, distance):
	x = entity.x
	y = entity.y

	neighbours = (
		Vector(-1, 0),
		Vector(1, 0),
		Vector(0, -1),
		Vector(0, 1)
	)

	stack = [Vector(x, y)]

	for i in range(distance):
		temp = []
		for x in stack:
			for y in neighbours:
				temp.append(x + y)
		stack.extend(temp)

	result = [(v.x, v.y) for v in vector.makeUniqueList(stack) if v.distance(entity) < distance]
	return [data[x][y] for x, y in result if x >= 0 and y >= 0 and x < len(data) and y < len(data[x])]

def getEntitiesByPosition(pos):
	return getEntitiesInPositions([pos])

def getEntitiesInPositions(pos_array):
	for x in getEntitiesInTiles(getTiles(pos_array)):
		yield x

def getEntitiesByTile(tile):
	return tile.entities

def getEntitiesInTiles(tiles):
	entities = []
	for tile in tiles:
		entities.extend(tile.entities)

	return entities

pass
