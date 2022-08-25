from enum import Enum
from pickle import TRUE
from grille import *
from pacman import *
from fantome import *
#from automate import Etat

class Etat:
    def __init__(self, Fr, Fb, Pac):
        self.Fr = Fantome(Fr.x,Fr.y)
        self.Fb = Fantome(Fb.x,Fb.y)
        self.Pac = Pacman(Pac.x,Pac.y)

def est_gagnant(etat):
    P=etat.Pac
    #print(P.x,',',P.y)
    Fr=etat.Fr 
    #print(Fr.x,',',Fr.y)
    Fb=etat.Fb 
    #print(Fb.x,',',Fb.y)
    return (P.x  == Fr.x and P.y == Fr.y) or (P.x == Fb.x and P.y == Fb.y)

def strategie(etat):

    x,y=0,0
    a,b=0,0

    if est_gagnant(etat) :
        #print("gagnant")
        return etat

    if etat.Fr.x - 1 <= etat.Pac.x <= etat.Fr.x + 1 :
        if etat.Fr.y==etat.Pac.y :
            if etat.Pac.x < etat.Fr.x :
                x,y = gauche(etat.Fr)
                
            else :
                x,y=droite(etat.Fr)
            
        elif etat.Fr.y < etat.Pac.y :
            x,y = bas(etat.Fr)

        else :
            x,y = haut(etat.Fr)   

    else :
        if etat.Pac.x < etat.Fr.x :
            x,y = gauche(etat.Fr)
        else :
            x,y = droite(etat.Fr)

    if etat.Fb.y - 1 <= etat.Pac.y <= etat.Fb.y + 1 :
        
        if etat.Fb.x==etat.Pac.x :
            if etat.Pac.y < etat.Fb.y :
                a,b = haut(etat.Fb)
            else :
                a,b = bas(etat.Fb)

        elif etat.Fb.x < etat.Pac.x :
            a,b = droite(etat.Fb)
        else :
            a,b = gauche(etat.Fb)
    
    else :
        if etat.Fb.y < etat.Pac.x :
            a,b = bas(etat.Fb)
        else :
            a,b = haut(etat.Fb)

    return Etat(Fantome(x,y),Fantome(a,b),etat.Pac)

def succ(etat,transition,gr):

    if est_gagnant(etat) :
        #print('gagnant')
        return []
    
    l=[] 

    e=transition(etat) #pacman ne fait rien
    
    l.append(e)

    x,y=haut(etat.Pac)
    if 0<x<=gr.largeur and 0<y<=gr.hauteur :
        e=transition(Etat(etat.Fr,etat.Fb,Pacman(x,y)))
        l.append(e)
    

    x,y=bas(etat.Pac)
    if 0<x<=gr.largeur and 0<y<=gr.hauteur :
        e=transition(Etat(etat.Fr,etat.Fb,Pacman(x,y)))
        l.append(e)

    x,y=droite(etat.Pac) 
    if 0<x<=gr.largeur and 0<y<=gr.hauteur :
        e=transition(Etat(etat.Fr,etat.Fb,Pacman(x,y)))
        l.append(e)

    x,y=gauche(etat.Pac)
    if 0<x<=gr.largeur and 0<y<=gr.hauteur :
        e=transition(Etat(etat.Fr,etat.Fb,Pacman(x,y)))
        l.append(e)

    return l

def detection_cycle(ens,transition,gr):

    pile_appel=[]
    deja_visite=[]

    for etat in ens :
        print("oui")
        l,ok = cycle_etat(etat,transition,pile_appel,deja_visite,gr)
        if ok :
            return l,True
    return [],False

def cycle_etat(etat,transition,pile_appel,deja_visite,gr):

    #print(len(succ(etat,transition,gr)))

    if etat in pile_appel :
        return [etat],True
    if etat in deja_visite :
        return [],False

    pile_appel.append(etat)
    deja_visite.append(etat)    

    
    for q in succ(etat,transition,gr) :
        l,ok=cycle_etat(q,transition,pile_appel,deja_visite,gr)
        if ok :
            print(len(l))
            return l.append(q),True
    pile_appel.remove(etat)
    return [],False
