import pyautogui as pg
import time
import math
import cv2 


def throw(angle_deg):
    O = [470, 887]
    r = 1200 - 960
    dx = r*math.sin(math.degrees(angle_deg))
    dy = r*math.cos(math.degrees(angle_deg))

    P = [O[0] + dx, O[1] + dy]
    
    pg.moveTo(x = P[0], y = P[1])
    # time.sleep(0.2)
    pg.drag(-dx, -dy, 0.11)
    # time.sleep(0.2)
    pg.mouseUp()
    
    # print(O, P)

if __name__ == "__main__":
    throw(-45)