import cv2
import numpy as np


def UpdateRGBColor(keycode, rgb_color):
    if ord('q') == keycode:
        rgb_color[0] += 1 if (rgb_color[0] + 1) <= 255 else 0
    elif ord('w') == keycode:
        rgb_color[1] += 1 if (rgb_color[1] + 1) <= 255 else 0
    elif ord('e') == keycode:
        rgb_color[2] += 1 if (rgb_color[2] + 1) <= 255 else 0
    elif ord('a') == keycode:
        rgb_color[0] -= 1 if (rgb_color[0] - 1) >= 0 else 0
    elif ord('s') == keycode:
        rgb_color[1] -= 1 if (rgb_color[1] - 1) >= 0 else 0
    elif ord('d') == keycode:
        rgb_color[2] -= 1 if (rgb_color[2] - 1) >= 0 else 0
    elif ord('r') == keycode:
        rgb_color[3] += 1 if (rgb_color[3] + 1) <= 255 else 0
    elif ord('t') == keycode:
        rgb_color[4] += 1 if (rgb_color[4] + 1) <= 255 else 0
    elif ord('y') == keycode:
        rgb_color[5] += 1 if (rgb_color[5] + 1) <= 255 else 0
    elif ord('f') == keycode:
        rgb_color[3] -= 1 if (rgb_color[3] - 1) >= 0 else 0
    elif ord('g') == keycode:
        rgb_color[4] -= 1 if (rgb_color[4] - 1) >= 0 else 0
    elif ord('h') == keycode:
        rgb_color[5] -= 1 if (rgb_color[5] - 1) >= 0 else 0
    else:
        return False
    return True

rgb_color = [128,0,0,255,235,205]
while True:
    img = cv2.imread('test.PNG')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    lower = (rgb_color[0], rgb_color[1], rgb_color[2])
    upper = (rgb_color[3], rgb_color[4], rgb_color[5])
    mask = cv2.inRange(hsv, lower, upper)

    keycode = cv2.waitKey(30)
    if UpdateRGBColor(keycode, rgb_color):
        print('lower({}), upper({})\n'.format(rgb_color[:3], rgb_color[3:]))

    cv2.imshow("Camera", img)
    cv2.imshow("mask", mask)