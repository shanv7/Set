import cv2
import numpy as np


def color(card):

    gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1, 1), 1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)
    imc, contour, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=cv2.contourArea, reverse=True)[1:2]

    M = cv2.moments(contour[0])
    contour = np.asarray(contour[0])
    row = int(contour.size/2)
    contour = np.reshape(contour, (row, 2))
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    for i in range(len(contour)):
        if contour[i, 0] <= cx:
            contour[i, 0] += 3
        else:
            contour[i, 0] -= 3
        if contour[i, 1] <= cy:
            contour[i, 1] += 3
        else:
            contour[i, 1] -= 3

    contour = contour.flatten()
    avg = np.array([0, 0, 0])
    for i in range(len(contour)):
        if not (i % 2):
            col = card[contour[i], contour[i+1]]
            avg += col
    avg = np.divide(avg, (len(contour)/2))

    if max(avg) == avg[1]:
        return 1    # Green
    elif max(avg) == avg[2] and np.std(avg) > 5:
        return 0    # Red
    else:
        return 2    # Purple
