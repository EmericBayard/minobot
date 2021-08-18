import pytesseract
import pyautogui
import time


from script import mapDetection
from script import utils
from script import deplacement
from script import saveMap
from script import peasant


def main():
    print("ok")
    # utils.initMinobot()
    # pyautogui.FAILSAFE = True
    # Map = saveMap.readList(saveMap.readMap('incarnam.txt', []), [])
    # Historic = [deplacement.getCoordinate()]
    # print("DEBUT DE L'EXPLORATION")
    # for i in range (0, 100):#28000 pour une nuit 6h
    #     deplacement.explore(Map, Historic)
    
    # saveMap.saveMap('incarnam.txt', Map)
    # saveMap.saveHistoric('historic.txt', Historic)
    
    peasant.tensWheat()
    # while True:
    #     x, y = pyautogui.position()
    #     positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #     print(positionStr, end='')
    #     print('\b' * len(positionStr), end='', flush=True)

if __name__ == "__main__":
    # execute only if run as a script
    main()