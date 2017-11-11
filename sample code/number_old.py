import cv2


def number(card):
    gray = cv2.cvtColor(card, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1, 1), 1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)
    imc, contour, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=cv2.contourArea, reverse=True)[1:4]
    length = len(contour)
    a0 = cv2.contourArea(contour[0])
    if length < 3:
        return length
    elif a0/cv2.contourArea(contour[1]) > 1.3:
        return 1
    elif a0/cv2.contourArea(contour[2]) > 1.3:
        return 2
    else:
        return 3
