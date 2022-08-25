from enum import Enum

class Orientation(Enum):
    Nord = 0
    Sud = 1
    Est = 2
    Ouest = 3
   
class Grille:
    def __init__(self, hauteur=5, largeur=7):
        self.hauteur = hauteur
        self.largeur = largeur

    def sommet(self):
        return(self.hauteur*self.largeur)
    
    def gr(self):
        return(range(self.hauteur*self.largeur))

def tourner_a_gauche (o):
    if o==Orientation.Nord :
        return Orientation.Ouest
    if o==Orientation.Sud :
        return Orientation.Est
    if o==Orientation.Est :
        return Orientation.Nord
    if o==Orientation.Ouest : 
        return Orientation.Sud

def tourner_a_droite (o):
    if o==Orientation.Nord :
        return Orientation.Est
    if o==Orientation.Sud :
        return Orientation.Ouest
    if o==Orientation.Est :
        return Orientation.Sud
    if o==Orientation.Ouest : 
        return Orientation.Nord

def avancer (o,x,y):
    if o==Orientation.Est :
        x=x+1
    if o==Orientation.Ouest :
        x=x-1
    if o==Orientation.Nord :
        y=y-1
    if o==Orientation.Sud :
        y=y+1

def point(fp,gr):
    return fp.x + fp.y*gr.largeur

def coordonee(p,gr):
    return p%gr.largeur,p//gr.largeur

def haut(FP):
    return FP.x,FP.y-1

def bas(FP):
    return FP.x,FP.y+1

def droite(FP):
    return FP.x+1,FP.y

def gauche(FP):
    return FP.x-1,FP.y
        