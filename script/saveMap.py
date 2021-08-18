import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from deplacement import Map
from mapDetection import getCoordinate
from datetime import datetime

#sauvegarde une liste dans un fichier
def saveMap(path, L):
    textfile = open(path, "w")
    for m in L:
        textfile.write(m.coordinate + "\n")
        textfile.write(str(m.trust_east)+"\n"+str(m.trust_west)+"\n"+str(m.trust_north)+"\n"+str(m.trust_south)+"\n")
    print("La map a bien été sauvegardé")
    textfile.close

def saveHistoric(path, L):
    textfile = open(path, "w")
    for m in L:
        textfile.write(m + "\n")
    print("L'historique a bien été sauvegardé")
    textfile.close

#lis le fichier et renvoi une liste de string
def readMap(path, L):
    with open(path) as f:
        lines = [line.rstrip() for line in f]
    return lines

#cast une liste de string en liste de map
def readList(L, Lres):
    for i in range (0, len(L)-1, 5):
        m = Map(L[i], int(L[i+1]), int(L[i+2]), int(L[i+3]), int(L[i+4]))
        Lres.append(m)
    return Lres