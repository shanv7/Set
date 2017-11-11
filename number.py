import cv2


def number(card):
    blurred = cv2.pyrMeanShiftFiltering(card, 12, 92)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    _, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    return len(contours)-1
