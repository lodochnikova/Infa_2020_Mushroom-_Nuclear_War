import pygame 
from drawing_module import del_bomb


class Bomb():
	def __init__(self, x: int, y: int, name: str):
		"""
		param: x, y - координата начала падение бомбы
		param: r - начальный радиус бомбы 
		param: time_of_life - убывает после каждого вызова функции drop_the_bomb()
		param: name - имя игрока, создающий бомбу, два варианта: bot and player 
		"""
		self.name_of_creater = name
		self.time_of_life = 200 
		self.x = x
		self.y = y
		self.r = 5
		self.color = 'black'
		self.create_bomb()

	def create_bomb(self):

		if self.name_of_creater == 'player':
			self.color = 'blue'
		if self.name_of_creater == 'bot':
			self.color = 'red'
		 

	def delete(self, x_player, y_player, name):
		"""
		Меняем текущие координаты бомбы на (-10, -10), тем самым бомба перемещается за холст
		x_player, y_player - координаты щелчка игрока 
		name - имя игрока унижтожающего цели, если совпадает self.name, то бомба не унижтожается 
		"""

		 # Щелчок находится в круге, еcли растояние до центра меньше радиуса этого круга 

		if self.name_of_creater != name:
			if (x_player - self.x) ** 2 + (y_player - self.y) ** 2 < self.r ** 2 :
				self.x = -10
				self.y = -10
				del_bomb(self.x, self.y )

	def drop_the_bomb(self):
		
		self.time_of_life -= 1
		self.r -= 1 

	def explodes(self, life_of_field):
		'''
			life_of_field - определяет жизнь вражеского поля
		'''
		life_of_field -= 10

		return life_of_field