from Bomb import *


class player():
    def __init__(self, name):
        self.name = name
        self.is_bot = False
        
    def bomb(self, x, y):
        return Bomb(x, y, self)


    def catch(self, x, y):
        bomb = find_bomb()
        bomb.delete(x, y, name)

    def repair(x, y):
        field.refit(name)
