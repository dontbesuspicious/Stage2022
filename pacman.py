from grille import Orientation as O

class Pacman:
    def __init__(self, x, y, o=O.Est):
        self.x = x
        self.y = y
        self.o = o

    def position(self):
        return self.x,self.y
