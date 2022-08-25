from grille import Orientation as O

class Fantome:
    def __init__(self, x=0, y=0, o=O.Est):
        self.x = x
        self.y = y
        self.o = o

    def position(self):
        return self.x,self.y
