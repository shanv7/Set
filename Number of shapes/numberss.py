import cv2
import numpy as np

image = cv2.imread('9.jpg')     #Change the image here

blurred = cv2.pyrMeanShiftFiltering(image,13,91)
#The parameters here are working for the sample images
#The first parameter is the spatial parameter and color parameter respectively
#The two parameters may change with other images

gray =cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray,155,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

_,contours,_ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print ("Number of contours detected %d"%(len(contours)-1))

cv2.drawContours(image,contours,-1,(0,0,255),6)
cv2.namedWindow('Display',cv2.WINDOW_NORMAL)
cv2.imshow('Display',image)
cv2.imshow('Displa',blurred)
cv2.imshow('Dspla',gray)
cv2.imshow('Dispa',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
