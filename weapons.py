class WeaponClass:
	DAGGER = 'dagger'
	STAFF = 'staff'
	BOW = 'bow'
	SWORD = 'sword'

WEAPON_LVLS = (
	(0, 10, 15, 20, 30, 75),
	(0, 15, 25, 30, 45, 150),
	(0, 20, 30, 40, 60, 400),
	(0, 30, 40, 50, 80, 800),
	(10, 40, 55, 70, 100, 1200),
	(20, 50, 70, 90, 120, 2000),
	(30, 60, 85, 110, 140, 3000),
	(40, 70, 100, 130, 160, 5000),
	(50, 80, 115, 150, 180, 8000),
	(70, 100, 150, 200, 230)
)

class Weapon(object):
	def __init__(self, data):
		self.weaponClass = data['class']
		self.AD = data['AD']
		self.MD = data['MD']
		self.LVL = data['LVL']
		self.name = data['name']
		self.description = data['description']

		self.AP = WEAPON_LVLS[self.LVL - 1][self.AD - 1]
		self.MAP = WEAPON_LVLS[self.LVL - 1][self.MD - 1]
		self.price = WEAPON_LVLS[self.LVL - 1][-1]

weapon_data = [{
	'class': "dagger",
	'name': "Knife",
	'LVL': 1,
	'AD': 3,
	'MD': 3,
	'special': None,
	'description': "This single-edged weapon is also handy for cutting your dinner."
}]

weapons = [Weapon(x) for x in weapon_data]
