import pyautogui
import time

def wereAmIonScreen():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def initMinobot():
    print("Starting", end="\n")
    for i in range (0,3):
        print(i, end="\n")
        time.sleep(1)
    print("Go !")