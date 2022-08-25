from enum import Enum
from itertools import combinations

from grille import *
from pacman import *
from fantome import *

class Tour(Enum):
    fan=0
    pac=1

class Etat:
    def __init__(self, F, P, T=Tour.fan):
        self.F = F
        self.P = P
        self.T = T
    def afficher(self):
        for i in self.F:
            print(i,end=',')

def ensemble_etat(f,gr):
    Q=[]
    Acc=[]

    l=combinations(gr.gr(),f)

    for i in l:
        for j in range(gr.sommet()):

            etat = Etat(i,j)
            Q.append(etat)

            if j in i:
                Acc.append(etat)
            
            etat.T = Tour.pac
            Q.append(etat)
            if j in i:
                Acc.append(etat)
    
    return Q,Acc

def transition(gr,etat,a='eps',nb_f=0):
    if etat.T==Tour.fan :
        x,y=coordonee(etat.F[nb_f],gr)
        #print(x,',',y)
        if a=='h':
            x,y=haut(x,y)

        if a=='b':
            x,y=bas(x,y)
            
        if a=='d':
            x,y=droite(x,y)
        
        if a=='g' :
            x,y=gauche(x,y)
        
        if a=='r' or a=='eps' :
            return [Etat(etat.F,etat.P,Tour.fan)]
            
        if x>=0 and y>=0 and x<gr.largeur and y<gr.hauteur :  
            #print(x,',',y)
            l=etat.F
            l[nb_f]=point(Fantome(x,y),gr)
            return [Etat(l,etat.P,Tour.pac)]
        else :
            return []
    else :
        l=[Etat(etat.F,etat.P)]
        x,y=coordonee(etat.P)

        x,y=haut(etat.P)
        if x>=0 and y>=0 and x<gr.largeur and y<gr.hauteur :
            l.append(Etat(etat.F,point(x,y,gr)))

        x,y=bas(etat.P)
        if x>=0 and y>=0 and x<gr.largeur and y>gr.hauteur :
            l.append(Etat(etat.F,point(x,y,gr)))
            
        x,y=droite(etat.P)
        if x>=0 and y>=0 and x<gr.largeur and y>gr.hauteur :
            l.append(Etat(etat.F,point(x,y,gr)))
        
        x,y=gauche(etat.P)
        if x>=0 and y>=0 and x<gr.largeur and y>gr.hauteur :
            l.append(Etat(etat.F,point(x,y,gr)))

        return l

def predecesseur(gr,etat):
    l=[]
    if etat.T==Tour.fan :
        p=etat.P+1
        if p>=0 and p<gr.sommet() :
            l.append(Etat(etat.F,p,Tour.pac))
        p=etat.P-1
        if p>=0 and p<gr.sommet() :
            l.append(Etat(etat.F,p,Tour.pac))
        p=etat.P + gr.largeur
        if p>=0 and p<gr.sommet() :
            l.append(Etat(etat.F,p,Tour.pac))
        p=etat.P - gr.largeur
        if p>=0 and p<gr.sommet() :
            l.append(Etat(etat.F,p,Tour.pac))
        return l

    else :
        comb=combinations(['h','b','d','g','r']*len(etat.F),len(etat.F))

        for i in comb :
            print(i)
            n=0
            for j in i :
                k=transition(gr,Etat(etat.F,etat.P),j,n)
                print(len(k))
                for e in k :
                    e.T=Tour.fan
                l.extend(k)
                n+=1
        return l
    
l=predecesseur(Grille(3,3),Etat([0],5,Tour.pac))

for i in l :
    print('( (',end='')
    for j in i.F :
        print(j,end=',')
    print(')',end='')
    print(',',i.P,',',end='')
    if i.T==Tour.fan :
        print('F)')
    else :
        print('P)')
