#!/usr/bin/python

import cv2
import numpy as np

numcards = 9
ids = np.zeros(4 * numcards)


im = cv2.imread('set.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (1, 1), 1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

imc, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:numcards]

for i in range(numcards):
    card = contours[i]

    # imc2, c2, h2, = cv2.findContours(card, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # c2 = sorted(contours, key=cv2.contourArea, reverse=True)[:numcards]
    # for j in c2:
        
    peri = cv2.arcLength(card, True)
    approx = np.array([cv2.approxPolyDP(card, 0.02 * peri, True)], np.float32)
    approx = approx.reshape(4, 2)
    rect = cv2.minAreaRect(contours[2])
    r = cv2.boxPoints(rect)
    h = np.array([[0, 0], [399, 0], [399, 599], [0, 599]], np.float32)
    transform = cv2.getPerspectiveTransform(approx, h)
    warp = cv2.warpPerspective(im, transform, (400, 600))
    cv2.namedWindow(str(i+1), cv2.WINDOW_NORMAL)
    cv2.imshow(str(i+1), warp)

cv2.waitKey(0)


# cv2.namedWindow('test', cv2.WINDOW_NORMAL)
# cv2.imshow('test', im2)
# cv2.waitKey(0)
