from strategie import *
import sys

sys.setrecursionlimit(10000)

#from itertools import combinations

l = 4 #= int(input('donnez la largeur du terrain'))
h = 4 #= int(input('donnez la hauteur du terrain'))

def fausse_strategie(etat) :
    return etat

G=Grille(h,l)

Fb = Fantome (1,h//2+1)

Fr = Fantome (l//2+1,1)


Q=[]

for i in range (1,l+1) :
    for j in range (1,h+1) :
        Pac = Pacman(i,j)
        Q.append(Etat(Fr,Fb,Pac)) 

print(len(Q))

l,ok=detection_cycle([Q[6]],strategie,G)

print("KWA")

if ok :
    print ('strat fausse')
else :
    print ('strat correct')


