class player():
    def __init__(self, name):
        self.name = name
        
    def bomb(self, x, y):
        Bomb(x, y, self.name)

    def catch(self, x, y):
        bomb = find_bomb()
        bomb.delete(x, y, name)

    def repair(x, y):
        field.refit(name)
