import pygame 

class Bomb():
	def __init__(self, x: int, y: int, id_creater):
		"""
		param: x, y - координата начала падение бомбы
		param: r - начальный радиус бомбы 
		param: time_of_life - убывает после каждого вызова функции drop_the_bomb()
		param: name - имя игрока, создающий бомбу, два варианта: bot and player 
		"""
		self.creater = id_creater
		self.time_of_life = 200 
		self.x = x
		self.y = y
		self.r = 5
		self.color = 'black'
		#self.create_bomb()

	#def create_bomb(self):

		#if self.creater.is_bot : # он всегда false для player, он выполянется для бота 
			#self.color = 'blue'
		#else:
			#self.color = 'red'
			
	def delete(self, x_click, y_click, id_creater):
		"""
		Меняем текущие координаты бомбы на (-10, -10), тем самым бомба перемещается за холст
		x_player, y_player - координаты щелчка игрока 
		name - имя игрока унижтожающего цели, если совпадает self.name, то бомба не унижтожается 
		"""

		 # Щелчок находится в круге, еcли растояние до центра меньше радиуса этого круга 

		if self.creater is not id_creater :# разные ссылки на  разные объекты creater
			if (x_click - self.x) ** 2 + (y_click - self.y) ** 2 < self.r ** 2 :
				self.x = -10
				self.y = -10


	def drop_the_bomb(self):
		
		self.time_of_life -= 1
		self.r -= 1 

	def explodes(self, life_of_field):
		'''
			life_of_field - определяет жизнь вражеского поля
		'''
		life_of_field -= 10

		return life_of_field