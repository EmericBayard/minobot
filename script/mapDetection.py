import pytesseract
import pyautogui
from cv2 import cv2 as cv


def getCoordinate():
    pyautogui.screenshot('screenshot.png',region=(0,83, 170, 60))
    scr = cv.imread('screenshot.png')
    mask_inv = cv.bitwise_not(scr)
    # cv.imshow('screen', mask_inv)
    # cv.waitKey(0)
    res = pytesseract.image_to_string(mask_inv)
    counter = 0
    final_res = ''
    for character in res:
        if character == ',':
            counter = counter + 1
        if counter >= 2:
            break
        final_res= final_res + character
    # print(final_res)
    return (final_res)


    