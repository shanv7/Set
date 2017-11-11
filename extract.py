import cv2
import numpy as np
import imutils


def extract(image, n):
    card = []
    image = str(image)
    im = cv2.imread(image)
    im = imutils.resize(im, height=1000)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1, 1), 1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

    imc, contour, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=cv2.contourArea, reverse=True)[:n]

    for i in range(n):
        peri = cv2.arcLength(contour[i], True)
        approx = cv2.approxPolyDP(contour[i], 0.02 * peri, True)
        pts = approx.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        dst = np.array([
            [0, 0],
            [399, 0],
            [399, 399],
            [0, 399]], dtype="float32")
        M = cv2.getPerspectiveTransform(rect, dst)
        warp = cv2.warpPerspective(im, M, (400, 400))
        card.append(warp)
    return card
