from Bomb import *


class Player():
    def __init__(self, name):
        self.name = name
        self.is_bot = False
        
    def bomb(self, x, y,t):
        return Bomb(x, y, self, t)


    def catch(self, x, y):
        bomb = find_bomb()
        bomb.delete(x, y, name)

    def repair(x, y):
        field.refit(name)
