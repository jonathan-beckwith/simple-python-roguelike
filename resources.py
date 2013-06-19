from pyglet import resource
from pyglet import image

resource.path = ['resource']
resource.reindex()

player_image = resource.image('player.png')
tiles_image = resource.image("tiles.png")
tiles_image_grid = image.ImageGrid(
	image=tiles_image,
	rows=19,
	columns=9
)
map_tiles = image.TextureGrid(tiles_image_grid)


monsters_image = resource.image("monster1.png")
monsters_grid = image.ImageGrid(
	image=monsters_image,
	rows=16,
	columns=6
)
monsters = image.TextureGrid(monsters_grid)

from pyglet import sprite
blue_overlay = sprite.Sprite(
			img=resource.image('blue_overlay.png'),
			x=0,
			y=0
		)