import random as r
import pyautogui
import time as t
from datetime import datetime
#ces lignes en dessous sont des solutions generiques pour importer entre ficheir
# d'un meme directory
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))


from mapDetection import getCoordinate

def goWest():
    x = r.randrange(158, 181, 1)
    y = r.randrange(0, 778,1)
    # s = r.uniform(5.0,8.0)
    # print("coordinate X : "+str(x)+" Y : "+str(y))
    pyautogui.click(x, y)
    # t.sleep(s)

def goNorth():
    x = r.randrange(187, 1255, 1)
    y = r.randrange(0, 14,1)
    # s = r.uniform(7.0,8.0)
    # print("coordinate X : "+str(x)+" Y : "+str(y))
    pyautogui.click(x, y)
    # t.sleep(s)

def goEast():
    x = r.randrange(1256, 1281, 1)
    y = r.randrange(0, 778,1)
    # s = r.uniform(5.0,8.0)
    # print("coordinate X : "+str(x)+" Y : "+str(y))
    pyautogui.click(x, y)
    # t.sleep(s)

def goSouth(): 
    x = r.randrange(220, 1170, 1)
    y = r.randrange(780, 798,1)
    # s = r.uniform(5.0,8.0)
    # print("coordinate X : "+str(x)+" Y : "+str(y))
    pyautogui.click(x, y)
    # t.sleep(s)

def isLocked(g1,g2):
    if g1 == g2:
        print("Le bot est bloqué en : "+ g2)
        g1 = 1
        g2 = 2
        return True
    print("Le bot n'est pas bloqué, position : "+ g2)
    g1 = 1
    g2 = 2
    return False

class Map():
    def __init__(self, coordinate, te, tw, tn, ts):
        self.coordinate = coordinate
        self.trust_east = te
        self.trust_west = tw
        self.trust_north = tn
        self.trust_south = ts

# pour l'historique, appelé avec une case au moins
def explore(L, H):
    s = r.uniform(7.0,8.0)
    currentMap = Map(getCoordinate(), 0, 0, 0, 0)
    hIndice = len(H) - 1
    #Historique
    if(currentMap.coordinate != H[hIndice]):
        H.append((currentMap.coordinate))
    #Savoir si je dois ajouter une entree a notre carte
    if(mapIsInList(L, currentMap)):
        print("Map is already traveled : "+ currentMap.coordinate)
        indice = findMap(L, currentMap.coordinate)
    else:
        print("Add a new map to our path : "+ currentMap.coordinate)
        L.append(currentMap)
        indice = len(L) - 1
    rand = r.randrange(1, 5, 1)
    if(L[indice].trust_north <= -3 and L[indice].trust_west <= -3  and L[indice].trust_south <= -3 and L[indice].trust_east <= -3):
        print("Bot is locked !!!")
    if(rand==1 and L[indice].trust_north > -50):
        g1 = getCoordinate()
        print("try to go north")
        goNorth()
        t.sleep(s)
        g2 = getCoordinate()
        if(isLocked(g1, g2)):
            L[indice].trust_north = L[indice].trust_north-1
        else:
            L[indice].trust_north = L[indice].trust_north+1
    elif(rand==2 and L[indice].trust_south > -50):
        g1 = getCoordinate()
        print("try to go south")
        goSouth()
        t.sleep(s)
        g2 = getCoordinate()
        if(isLocked(g1, g2)):
            L[indice].trust_south = L[indice].trust_south-1
        else:
            L[indice].trust_south = L[indice].trust_south+1
    elif(rand==3 and L[indice].trust_east > -50):
        g1 = getCoordinate()
        print("try to go east")
        goEast()
        t.sleep(s)
        g2 = getCoordinate()
        if(isLocked(g1, g2)):
            L[indice].trust_east = L[indice].trust_east-1
        else:
            L[indice].trust_east = L[indice].trust_east+1
    elif(rand==4 and L[indice].trust_west > -50):
        g1 = getCoordinate()
        print("try to go west")
        g2 = getCoordinate()
        goWest()
        t.sleep(s)
        if(isLocked(g1, g2)):
            L[indice].trust_west = L[indice].trust_west-1
        else:
            L[indice].trust_west = L[indice].trust_west+1


    


    

    
# def isTraveled(Array):

def mapInList(L):
    for m in L:
        print(m.coordinate)
        print("trust level on east : "+str(m.trust_east))
        print("trust level on north : "+str(m.trust_north))
        print("trust level on west : "+str(m.trust_west))
        print("trust level on south : "+str(m.trust_south))

def mapIsInList(L, M):
    for m in L:
        if(m.coordinate == M.coordinate):
            return True
    return False

def findMap(L, coord):
    i = 0
    for m in L:
        if(m.coordinate == coord):
            return i
        i = i + 1




    
